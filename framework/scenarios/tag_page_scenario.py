from framework.ports.browser_port import BrowserPort
from framework.adapters.locators.tag_page_locators import TagPageLocators

class TagPageScenario:
  """
  Lógica de negocio para interactuar con la página de tags.
  """

  def __init__(self, browser: BrowserPort):
    self._browser = browser
    self.tag_page = TagPageLocators

  def verify_tag_page_loaded(self, tag_name: str) -> bool:
    """
    Verifica que la página de un tag haya cargado correctamente.
    """
    page_title = self._browser.get_text(self.tag_page.tagPageTitle)
    return tag_name in page_title