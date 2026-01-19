from framework.ports.browser_port import BrowserPort
from framework.adapters.locators.home_page_locators import HomePageLocators
from framework.adapters.locators.common_locators import CommonLocators
from framework.adapters.locators.post_card_locators import PostCardLocators
from framework.adapters.locators.post_metadata_locators import PostMetadataLocators

class HomePageScenario:
  """
  Lógica de negocio para interactuar con la página Home.

  Responsabilidades:
    - Verificar que componentes del home page cargan.
    - Obtener datos de featured post y recent posts.
    - Interactuar con posts para navegación.
  """

  def __init__(self, browser: BrowserPort):
    self._browser = browser

  # Verificaciones de carga
  def verify_home_loaded(self) -> bool:
    """ Verifica que la página Home cargó (usa site logo como indicador)."""
    return self._browser.is_visible(CommonLocators.siteLogo)

  def verify_hero_section_loaded(self) -> bool:
    """Verifica que la hero section está visible."""
    return self._browser.is_visible(HomePageLocators.heroSection)

  def verify_footer_loaded(self) -> bool:
    """ Verifica que el footer está visible."""
    return self._browser.is_visible(CommonLocators.footerContainer)

  def verify_navbar_is_visible(self) -> bool:
    """Verifica que la barra de navegación está visible."""
    return self._browser.is_visible(CommonLocators.navbarContainer)

  def verify_theme_toggle_is_visible(self) -> bool:
    """Verifica que el toggle de tema está visible en la navbar."""
    return self._browser.is_visible(CommonLocators.navbarThemeToggle)

  def verify_featured_post_is_shown(self) -> bool:
    """Verifica que el featured post está visible."""
    return self._browser.is_visible(HomePageLocators.featuredPostCard)

  def verify_recent_posts_are_listed(self) -> bool:
    """Verifica que la sección de recent posts está visible."""
    return self._browser.is_visible(HomePageLocators.recentPostsList)

  # Obtención de datos
  def get_featured_post_data(self) -> dict:
    """
    Obtiene los datos del post destcado.

    Returns: diccionario con keys: title, summary, date

    Raises:
      TimeoutError: Si el featured post no está visible.
    """
    return {
      'title': self._browser.get_text(HomePageLocators.featuredPostTitle),
      'summary': self._browser.get_text(HomePageLocators.featuredPostSummary),
      'date': self._browser.get_text(f"{HomePageLocators.featuredPostCard} {PostMetadataLocators.postDate}")
      }

  def get_recent_post_titles(self) -> list[str]:
    """
    Obtiene los títulos de los posts recientes.

    Returns: Lista de títulos de posts (strings).

    Raises:
      TimeoutError: Si la sección de recent posts no está visible.
    """
    title_locator = f"{PostCardLocators.postCardContainer} {PostCardLocators.postCardTitle}"
    return self._browser.get_all_texts(title_locator)

  # Interacciones
  def open_featured_post(self) -> None:
    """
    Hace click en el featured post para navegar a su pagina.

    Raises:
      TimeoutError: Si el featured post no está visible.
    """
    self._browser.click(HomePageLocators.featuredPostTitle)

  def open_most_recent_post(self) -> None:
    """
    Hace click en el post más reciente de la sección recent posts.

    Raises:
      TimeoutError: Si la sección de recent posts no está visible.
    """
    first_post_title = f"{PostCardLocators.postCardContainer} >> nth=0 >> {PostCardLocators.postCardTitle}"
    self._browser.click(first_post_title)


