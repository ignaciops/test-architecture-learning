pytest_plugins = ["tests.fixtures.mobile_fixtures"]

import pytest
import allure

from playwright.sync_api import Page
from framework.adapters.playwright.browser_adapter import PlaywrightBrowserAdapter
from framework.scenarios.navigation_scenario import NavigationScenario
from framework.scenarios.home_page_scenario import HomePageScenario
from framework.scenarios.post_page_scenario import PostPageScenario
from framework.scenarios.blog_listing_scenario import BlogListingScenario
from framework.scenarios.tag_page_scenario import TagPageScenario

# Imports para implementacion Fake
from framework.adapters.fake.fake_browser_adapter import FakeBrowserAdapter
from framework.adapters.locators.common_locators import CommonLocators
from framework.adapters.locators.blog_page_locators import BlogPageLocators
from framework.adapters.locators.post_card_locators import PostCardLocators
from framework.adapters.locators.post_metadata_locators import PostMetadataLocators

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

@pytest.fixture
def tag_page_scenario(browser_port) -> TagPageScenario:
  """
  Fixture que provee el scenario de la página de tags con la dependencia inyectada.
  """
  return TagPageScenario(browser_port)


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
    page = None
    for fixture_name, fixture_value in item.funcargs.items():
      if isinstance(fixture_value, Page):
        page = fixture_value
        break

    if not page:
      page = item.funcargs.get("page") or \
             item.funcargs.get("mobile_page") or \
             item.funcargs.get("tablet_page")

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

# Fixtures para FakeBrowserAdapter
@pytest.fixture
def fake_browser_with_complete_posts():
  """
  FakeBrowserAdapter con blog listing completo
  3 posts con metadata completa.
  """
  dom_state = {
    CommonLocators.navbarBlogLink: {
      "text": "Blog",
      "visible": True
    },

    # Blog page
    BlogPageLocators.blogPageTitle: {
      "text": "Blog",
      "visible": True
    },
    PostCardLocators.postCardContainer: {
      "count":3,
      "visible": True
    },

    # Datos estructurados
    f"structured_data:{PostCardLocators.postCardContainer}": [
            {
                "title": "Post 1: Architecture Patterns",
                "date": "2026-01-15",
                "summary": "Learning hexagonal architecture",
                "readingTime": "5 min"
            },
            {
                "title": "Post 2: Testing Strategy",
                "date": "2026-01-10",
                "summary": "Defining test approach",
                "readingTime": "7 min"
            },
            {
                "title": "Post 3: Playwright Tips",
                "date": "2026-01-05",
                "summary": "Advanced Playwright techniques",
                "readingTime": "6 min"
            }
    ],

  }
  return FakeBrowserAdapter(dom_state)

@pytest.fixture
def blog_listing_scenario_with_fake(fake_browser_with_complete_posts):
  """
  Fixture que devuelve tupla (scenario, fake_browser)
  """

  scenario = BlogListingScenario(fake_browser_with_complete_posts)
  return scenario, fake_browser_with_complete_posts

@pytest.fixture
def fake_browser_with_incomplete_metadata():
    """
    FakeBrowserAdapter con posts que tienen metadata incompleta.
    """
    dom_state = {
        BlogPageLocators.blogPageTitle: {
            "text": "Blog",
            "visible": True
        },

        PostCardLocators.postCardContainer: {
          "count": 2,
          "visible": True
        },

        f"structured_data:{PostCardLocators.postCardContainer}": [
            {
                "title": "Post sin fecha",
                "date": "",  # ← FALTA fecha
                "summary": "Some summary",
                "readingTime": "5 min"
            },
            {
                "title": "Post sin reading time",
                "date": "2026-01-15",
                "summary": "Another summary",
                "readingTime": ""  # ← FALTA reading time
            }
        ]
    }

    return FakeBrowserAdapter(dom_state)

@pytest.fixture
def fake_browser_empty():
    """
    FakeBrowserAdapter sin posts (blog vacío).
    """
    dom_state = {
        BlogPageLocators.blogPageTitle: {
            "text": "Blog",
            "visible": True
        },
        PostCardLocators.postCardContainer: {
          "count": 0,
          "visible": True
        },
        f"structured_data:{PostCardLocators.postCardContainer}": []
        # No hay post cards
    }

    return FakeBrowserAdapter(dom_state)