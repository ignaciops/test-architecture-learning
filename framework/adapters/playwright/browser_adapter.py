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

    def navigate_to(self, url: str) -> None:
        self._page.goto(url)

    def click(self, locator: str) -> None:
        self._page.locator(locator).click()

    def get_text(self, locator: str) -> str:
        return self._page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self._page.locator(locator).is_visible()

    def get_all_texts(self, locator: str) -> list[str]:
        return self._page.locator(locator).all_inner_texts()

    def get_element_count(self, locator: str) -> int:
        return self._page.locator(locator).count()

    def wait_for_element(self, locator: str, timeout: int = 10000) -> None:
        self._page.locator(locator).wait_for(state="visible", timeout=timeout)

    def wait_for_load_state(self, state: str = "networkidle") -> None:
        self._page.wait_for_load_state(state)