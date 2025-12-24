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