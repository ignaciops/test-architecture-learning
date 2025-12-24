import pytest
from playwright.sync_api import Page
from framework.adapters.playwright.browser_adapter import PlaywrightBrowserAdapter
from framework.scenarios.navigation_scenario import NavigationScenario

@pytest.fixture
def browser_port(page: Page) -> PlaywrightBrowserAdapter:
  """
  Fixture que provee la implementacion concreta del BrowserPort.
  """
  return PlaywrightBrowserAdapter(page)

@pytest.fixture
def navigation_scenario(browser_port) -> NavigationScenario:
  """
  Fixture que provee el scenario con la dependencia inyectada.
  """
  return NavigationScenario(browser_port)