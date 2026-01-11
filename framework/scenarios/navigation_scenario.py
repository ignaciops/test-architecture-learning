from framework.ports.browser_port import BrowserPort
from framework.adapters.locators.home_page_locators import HomePageLocators
from framework.adapters.locators.common_locators import CommonLocators
from framework.infrastructure.config import Config

class NavigationScenario:
  """
  Lógica de negocio para navegación entre páginas.

  Usa el navbar para moverse entre páginas principales del sitio.
  """

  def __init__(self, browser: BrowserPort):
    self._browser = browser

  def navigate_to_home(self) -> None:
    """Navega a la página Home del blog."""
    self._browser.navigate_to(Config.BASE_URL)
    self._browser.wait_for_load_state("networkidle")

  def navigate_to_projects(self) -> None:
    """Navega a la página de Proyectos."""
    self._browser.click(CommonLocators.navbarProyectosLink)
    self._browser.wait_for_load_state("networkidle")

  def navigate_to_blog(self) -> None:
    """Navega a la página del Blog."""
    self._browser.click(CommonLocators.navbarBlogLink)
    self._browser.wait_for_load_state("networkidle")

  def navigate_to_about(self) -> None:
    """Navega a la página Acerca de."""
    self._browser.click(CommonLocators.navbarAcercaLink)
    self._browser.wait_for_load_state("networkidle")