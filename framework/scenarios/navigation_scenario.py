from framework.ports.browser_port import BrowserPort

class NavigationScenario:
  """
  Lógica de negocio.
  """

  def __init__(self, browser: BrowserPort):
    self._browser = browser

  def go_to_home(self, url: str) -> None:
    self._browser.navigate_to(url)

  def verify_home_loaded(self) -> bool:
    return self._browser.is_visible('[data-testid="blog-title"]')