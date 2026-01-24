from framework.ports.browser_port import BrowserPort
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
    self._browser.click_navigation_link("projects")
    self._browser.wait_for_load_state("networkidle")

  def navigate_to_blog(self) -> None:
    """Navega a la página del Blog."""
    self._browser.click_navigation_link("blog")
    self._browser.wait_for_load_state("networkidle")

  def navigate_to_about(self) -> None:
    """Navega a la página Acerca de."""
    self._browser.click_navigation_link("about")
    self._browser.wait_for_load_state("networkidle")