import pytest
import allure
from playwright.sync_api import Page, Browser, Playwright
from framework.adapters.playwright.browser_adapter import PlaywrightBrowserAdapter
from framework.scenarios.navigation_scenario import NavigationScenario
from framework.scenarios.home_page_scenario import HomePageScenario
from framework.scenarios.post_page_scenario import PostPageScenario
from framework.scenarios.blog_listing_scenario import BlogListingScenario


# Page fixtures
@pytest.fixture
def mobile_page(browser: Browser, playwright: Playwright) -> Page:
    """
    Page instance configurada para mobile viewport.
    Esta es la base para los mobile_* scenarios.
    """
    iphone = playwright.devices["iPhone 11"]
    context = browser.new_context(**iphone)
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def mobile_large_page(browser: Browser, playwright: Playwright) -> Page:
    """
    Page instance configurada para mobile large viewport.
    """
    iphone = playwright.devices["iPhone 13 Pro Max"]
    context = browser.new_context(**iphone)
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def tablet_page(browser: Browser, playwright: Playwright) -> Page:
    """
    Page instance configurada para tablet viewport
    """
    ipad = playwright.devices["iPad Mini"]
    context = browser.new_context(**ipad)
    page = context.new_page()
    yield page
    context.close()


# Browser Port fixtures

@pytest.fixture
def mobile_browser_port(mobile_page: Page) -> PlaywrightBrowserAdapter:
    """
    Fixture que provee la implementacion de BrowserPort para mobile viewport
    """
    return PlaywrightBrowserAdapter(mobile_page)

@pytest.fixture
def tablet_browser_port(tablet_page: Page) -> PlaywrightBrowserAdapter:
    """
    Fixture que provee la implementacion de BrowserPort para tablet viewport
    """
    return PlaywrightBrowserAdapter(tablet_page)

# Scenario Fixtures para mobile

@pytest.fixture
def mobile_navigation_scenario(mobile_browser_port) -> NavigationScenario:
    """
    NavigationScenario para mobile viewport
    """
    return NavigationScenario(mobile_browser_port)

@pytest.fixture
def mobile_home_page_scenario(mobile_browser_port) -> HomePageScenario:
    """
    HomePageScenario para mobile viewport
    """
    return HomePageScenario(mobile_browser_port)

@pytest.fixture
def mobile_blog_listing_scenario(mobile_browser_port) -> BlogListingScenario:
    """
    BlogListingScenario para mobile viewport
    """
    return BlogListingScenario(mobile_browser_port)

@pytest.fixture
def mobile_blog_listing_page_loaded(mobile_navigation_scenario, mobile_blog_listing_scenario):
  """
  Fixture que navega a la página de listado de blog y verifica que haya cargado correctamente.
  """
  with allure.step("Navegar a la página de listado de blog"):
    mobile_navigation_scenario.navigate_to_home()
    mobile_navigation_scenario.navigate_to_blog()
    assert mobile_blog_listing_scenario.verify_blog_listing_loaded(), "La página de listado de blog no cargó correctamente."

  return mobile_blog_listing_scenario

@pytest.fixture
def mobile_post_page_scenario(mobile_browser_port) -> PostPageScenario:
    """
    PostPageScenario para mobile viewport
    """
    return PostPageScenario(mobile_browser_port)

# Scenario Fixtures para tablet

@pytest.fixture
def tablet_navigation_scenario(tablet_browser_port) -> NavigationScenario:
    """
    NavigationScenario para tablet viewport
    """
    return NavigationScenario(tablet_browser_port)

@pytest.fixture
def tablet_home_page_scenario(tablet_browser_port) -> HomePageScenario:
    """
    HomePageScenario para tablet viewport
    """
    return HomePageScenario(tablet_browser_port)

@pytest.fixture
def tablet_blog_listing_scenario(tablet_browser_port) -> BlogListingScenario:
    """
    BlogListingScenario para tablet viewport
    """
    return BlogListingScenario(tablet_browser_port)

@pytest.fixture
def tablet_post_page_scenario(tablet_browser_port) -> PostPageScenario:
    """
    PostPageScenario para tablet viewport
    """
    return PostPageScenario(tablet_browser_port)
