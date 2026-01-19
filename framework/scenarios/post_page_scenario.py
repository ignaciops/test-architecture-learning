from framework.ports.browser_port import BrowserPort
from framework.adapters.locators.post_page_locators import PostPageLocators
from framework.adapters.locators.post_metadata_locators import PostMetadataLocators

class PostPageScenario:
  """
  Lógica de negocio para interactuar con la página de un post individual.

  Responsabilidades:
    - Verificar que componentes del post page cargan.
    - Obtener datos del post (título, autor, fecha, contenido).
  """

  def __init__(self, browser: BrowserPort):
    self._browser = browser

  # Verificaciones de carga
  def verify_post_page_loaded(self) -> bool:
    """Verifica que la página del post cargó (usa el header del post como indicador)."""
    return self._browser.is_visible(PostPageLocators.postHeaderSection)

  def verify_publication_date_is_visible(self) -> bool:
    """Verifica que la fecha de publicación está visible."""
    return self._browser.is_visible(PostMetadataLocators.postDate)

  def verify_content_is_visible(self) -> bool:
    """Verifica que el contenido del post está visible."""
    return self._browser.is_visible(PostPageLocators.postContentSection)

  # Obtención de datos del post
  def get_post_title(self) -> str:
    """
    Obtiene el título del post.

    Returns: título del post como string.

    Raises:
      TimeoutError: Si el título del post no está visible.
    """
    return self._browser.get_text(PostPageLocators.postTitle)

  def get_publication_date(self) -> str:
    """
    Obtiene la fecha de publicación del post.

    Returns: fecha de publicación como string.

    Raises:
      TimeoutError: Si la fecha de publicación no está visible.
    """
    return self._browser.get_text(PostMetadataLocators.postDate)

  def get_reading_time(self) -> str:
    """
    Obtiene el tiempo estimado de lectura del post.

    Returns: tiempo de lectura como string.

    Raises:
      TimeoutError: Si el tiempo de lectura no está visible.
    """
    return self._browser.get_text(PostMetadataLocators.postReadTime)

  def get_post_summary(self) -> str:
    """
    Obtiene el resumen del post.

    Returns: resumen del post como string.

    Raises:
      TimeoutError: Si el resumen del post no está visible.
    """
    return self._browser.get_text(f"{PostPageLocators.postHeaderSection} p")