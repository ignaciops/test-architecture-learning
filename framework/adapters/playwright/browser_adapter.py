# framework/adapters/playwright/browser_adapter.py
from playwright.sync_api import Page
from framework.ports.browser_port import BrowserPort
from framework.adapters.locators.common_locators import CommonLocators

class PlaywrightBrowserAdapter(BrowserPort):
    """
    Implementación del BrowserPort usando Playwright.

    Análogo a TypeScript:
    class PlaywrightAdapter implements BrowserPort { ... }
    """

    def __init__(self, page: Page):
        self._page = page
        self._is_mobile = self._detect_mobile_viewport()
        self._default_timeout = 10000 if self._is_mobile else 5000

    def _detect_mobile_viewport(self) -> bool:
        """
        Detecta automaticamente si se usa un dispositivo movil.

        Returns:
            True si viewport width < 768px, False en caso contrario
        """
        viewport = self._page.viewport_size
        return viewport["width"] < 768 if viewport else False

    # Navegación básica
    def navigate_to(self, url: str) -> None:
        self._page.goto(url)

    def wait_for_load_state(self, state: str = "networkidle") -> None:
        self._page.wait_for_load_state(state)

    # Interacciones con un elemento
    def click(self, locator: str) -> None:
        self._page.locator(locator).click()

    def get_text(self, locator: str) -> str:
        return self._page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        try:
            element = self._page.locator(locator)
            element.wait_for(state="visible", timeout=self._default_timeout)
            return element.is_visible()
        except Exception:
            return False

    def wait_for_element(self, locator: str, timeout: int = 10000) -> None:
        self._page.locator(locator).wait_for(state="visible", timeout=timeout)

    def click_navigation_link(self, link_identifier: str) -> None:
        """
        Implementacion que maneja navegacion desktop vs mobile.

        Mobile: abre hamburger menu primero, luego hace clik en link
        Desktop: hace click directo en navbar
        """
        if self._is_mobile:
            self._page.wait_for_load_state("networkidle")
            hamburger = self._page.locator(CommonLocators.mobileMenuToggle)
            mobile_menu = self._page.locator(CommonLocators.mobileMenu)

            hamburger.wait_for(state="visible", timeout=5000)

            if not mobile_menu.is_visible():
                hamburger.click()

                if not mobile_menu.is_visible():
                    self._page.evaluate("""
                    () => {
                        const menu = document.querySelector('[data-testid="mobile-menu"]');
                        if (menu) {
                            menu.classList.remove('hidden');
                            menu.classList.add('visible');
                        }

                        const btn = document.querySelector('[data-testid="mobile-menu-toggle"]');
                        if (btn) {
                            btn.setAttribute('aria-expanded', 'true');
                        }

                        // También cambiar los iconos
                        const openIcon = document.getElementById('menu-icon-open');
                        const closeIcon = document.getElementById('menu-icon-close');
                        if (openIcon) openIcon.classList.add('hidden');
                        if (closeIcon) closeIcon.classList.remove('hidden');
                    }
                """)
                mobile_menu.wait_for(state="visible", timeout=2000)

            link_map = {
                "blog": CommonLocators.mobileBlogLink,
                "projects": CommonLocators.mobileProyectosLink,
                "about": CommonLocators.mobileAcercaLink
            }

            link_locator = link_map.get(link_identifier)
            if not link_locator:
                raise ValueError(f"Link Identifier '{link_identifier}' no reconocido")

            self._page.locator(link_locator).click()
        else:
            link_map = {
                "blog" : CommonLocators.navbarBlogLink,
                "projects": CommonLocators.navbarProyectosLink,
                "about": CommonLocators.navbarAcercaLink,
            }

            link_locator = link_map.get(link_identifier)
            if not link_locator:
                raise ValueError(f"Link Identifier '{link_identifier}' no reconocido")

            self._page.locator(link_locator).click()

    # Interacciones con múltiples elementos

    def get_all_texts(self, locator: str) -> list[str]:
        return self._page.locator(locator).all_inner_texts()

    def get_element_count(self, locator: str) -> int:
        return self._page.locator(locator).count()

    # Operaciones con elementos anidados
    def get_text_from_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> str:
        parent_element = self._page.locator(parent_locator).all()

        if parent_index >= len(parent_element):
            raise IndexError(
                f"Parent index {parent_index} out of range."
                f"Only {len(parent_element)} elements found."
            )

        parent = parent_element[parent_index]
        child = parent.locator(child_locator)

        text = child.text_content()
        return text.strip() if text else ""

    def click_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> None:
        parent_element = self._page.locator(parent_locator).all()

        if parent_index >= len(parent_element):
            raise IndexError(
                f"Parent index {parent_index} out of range."
                f"Only {len(parent_element)} elements found."
            )

        parent = parent_element[parent_index]
        parent.locator(child_locator).click()

    def get_all_nested_texts(
        self,
        parent_locator: str,
        child_locator: str
    ) -> list[str]:
        parent_element = self._page.locator(parent_locator).all()

        texts = []
        for parent in parent_element:
            child = parent.locator(child_locator)
            text = child.text_content()
            if text:
                texts.append(text.strip())

        return texts

    def get_structured_data(
        self,
        parent_locator: str,
        field_selectors: dict[str, str]
    ) -> list[dict[str, str]]:
        parent_element = self._page.locator(parent_locator).all()

        data = []
        for parent in parent_element:
            item = {}
            for field_name, child_selector in field_selectors.items():
                child = parent.locator(child_selector)
                text = child.text_content()
                item[field_name] = text.strip() if text else ""
            data.append(item)

        return data

    def get_all_texts_from_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> list[str]:
        parent_element = self._page.locator(parent_locator).all()

        if parent_index >= len(parent_element):
            raise IndexError(
                f"Parent index {parent_index} out of range."
                f"Only {len(parent_element)} elements found."
            )

        parent = parent_element[parent_index]
        children = parent.locator(child_locator).all()

        return [
            child.text_content().strip() for child in children if child.text_content()
        ]