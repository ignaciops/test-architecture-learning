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

# Hook para agregar capturas de pantalla on failure y agregarlos a Allure report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
  """
  Hook que detecta fallos y marca la página para screenshot.
  Se ejecuta después de cada fase del test (setup, call, teardown).
  """
  outcome = yield
  rep = outcome.get_result()

  if rep.when == "call" and rep.failed:
    page: Page = item.funcargs.get("page")
    if page:
      try:
        screenshot_bytes = page.screenshot()
        allure.attach(
          screenshot_bytes,
          name=f"screenshot_on_failure_{item.name}",
          attachment_type=allure.attachment_type.PNG
        )
      except Exception as e:
        print(f"Error tomando screenshot: {e}")
