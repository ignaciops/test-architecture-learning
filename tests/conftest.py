import pytest
import allure
from playwright.sync_api import Page
from framework.adapters.playwright.browser_adapter import PlaywrightBrowserAdapter
from framework.scenarios.navigation_scenario import NavigationScenario
from framework.scenarios.home_page_scenario import HomePageScenario
from framework.scenarios.post_page_scenario import PostPageScenario
from framework.scenarios.blog_listing_scenario import BlogListingScenario

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

@pytest.fixture
def blog_listing_scenario(browser_port) -> BlogListingScenario:
  """
  Fixture que provee el scenario de la página de listado de blog con la dependencia inyectada.
  """
  return BlogListingScenario(browser_port)

@pytest.fixture
def blog_listing_page_loaded(navigation_scenario, blog_listing_scenario):
  """
  Fixture que navega a la página de listado de blog y verifica que haya cargado correctamente.
  """
  with allure.step("Navegar a la página de listado de blog"):
    navigation_scenario.navigate_to_home()
    navigation_scenario.navigate_to_blog()
    assert blog_listing_scenario.verify_blog_listing_loaded(), "La página de listado de blog no cargó correctamente."

  return blog_listing_scenario