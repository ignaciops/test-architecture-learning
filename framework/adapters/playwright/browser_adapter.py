# framework/adapters/playwright/browser_adapter.py
from playwright.sync_api import Page
from framework.ports.browser_port import BrowserPort

class PlaywrightBrowserAdapter(BrowserPort):
    """
    Implementación del BrowserPort usando Playwright.

    Análogo a TypeScript:
    class PlaywrightAdapter implements BrowserPort { ... }
    """

    def __init__(self, page: Page):
        self._page = page

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
        return self._page.locator(locator).is_visible()

    def wait_for_element(self, locator: str, timeout: int = 10000) -> None:
        self._page.locator(locator).wait_for(state="visible", timeout=timeout)

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