import pytest
from playwright.sync_api import Page
from framework.adapters.playwright.browser_adapter import PlaywrightBrowserAdapter
from framework.scenarios.navigation_scenario import NavigationScenario
from framework.scenarios.home_page_scenario import HomePageScenario
from framework.scenarios.post_page_scenario import PostPageScenario

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

@pytest.fixture
def home_page_scenario(browser_port) -> HomePageScenario:
  """
  Fixture que provee el scenario de la página Home con la dependencia inyectada.
  """
  return HomePageScenario(browser_port)

@pytest.fixture
def post_page_scenario(browser_port) -> PostPageScenario:
  """
  Fixture que provee el scenario de la página de un post con la dependencia inyectada.
  """
  return PostPageScenario(browser_port)