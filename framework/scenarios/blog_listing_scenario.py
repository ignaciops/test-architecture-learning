from framework.ports.browser_port import BrowserPort
from framework.adapters.locators.blog_page_locators import BlogPageLocators
from framework.adapters.locators.post_metadata_locators import PostMetadataLocators
from framework.adapters.locators.post_card_locators import PostCardLocators

class BlogListingScenario:
  """
  Lógica de negocio para interactuar con los listados de blog posts.
  """

  def __init__(self, browser: BrowserPort):
    self._browser = browser
    self.blog_page = BlogPageLocators
    self.post_card = PostCardLocators
    self.post_metadata = PostMetadataLocators

  def verify_blog_listing_loaded(self) -> bool:
    """
    Verifica que la página de listado de blog haya cargado correctamente.

    Returns:
        bool: True si la página cargó correctamente, False en caso contrario.
    """
    return self._browser.is_visible(self.blog_page.blogPageTitle)

  def get_all_post_titles(self) -> list[str]:
    """
    Obtiene los titulos de todos los posts listados en la página de blog.

    Returns:
        list[str]: Lista de titulos en el orden en que aparecen.
    """
    return self._browser.get_all_nested_texts(
      self.post_card.postCardContainer,
      self.post_card.postCardTitle
    )

  def get_post_count(self) -> int:
    """
    Obtiene la cantidad de posts listados en la página de blog.

    Returns:
        int: Cantidad de posts.
    """
    return self._browser.get_element_count(
      self.post_card.postCardContainer
    )

  def get_post_metadata(self, index:int) -> dict[str, str]:
    """
    Obtiene los metadatos (titulo, fecha, summary, tiempo de lectura) de un post específico.

    Args:
        index (int): Índice del post en el listado (0-based).

    Returns:
        dict[str, str]: Diccionario con los metadatos del post.
    """
    metadata = self._browser.get_structured_data(
      self.post_card.postCardContainer,
      {
        "title": self.post_card.postCardTitle,
        "date": self.post_metadata.postDate,
        "summary": self.post_card.postCardSummary,
        "readingTime": self.post_metadata.postReadTime
      }
    )

    if index >= len(metadata):
      raise IndexError(
        f"Post index {index} out of range."
        f"Only {len(metadata)} posts found."
      )

    return metadata[index]

  def open_post_by_index(self, index: int) -> None:
    """
    Abre un post específico en el listado por su índice.

    Args:
        index (int): Índice del post en el listado (0-based).
    """
    posts_count = self.get_post_count()

    if index >= posts_count:
      raise IndexError(
        f"Cannot open post at index {index}."
        f"Only {posts_count} posts available."
      )

    self._browser.click_nested(
      self.post_card.postCardContainer,
      self.post_card.postCardTitle,
      index
    )

  def open_post_by_title(self, title: str) -> None:
    """
    Abre un post por su título siempre y cuando exista en el listado presente.
    Args:
        title (str): Título del post a abrir.
    """
    titles = self.get_all_post_titles()

    try:
      index = titles.index(title)
      self.open_post_by_index(index)
    except ValueError:
      raise ValueError(f"No post found with title: {title}")

  def verify_all_posts_have_metadata(self) -> bool:
    """
    Verifica que todos los posts tengan los metadatos minimos necesarios:
    Titulo, Fecha, Tiempo de lectura y Summary.
    """
    all_metadata = self._browser.get_structured_data(
      self.post_card.postCardContainer,
      {
        "title": self.post_card.postCardTitle,
        "date": self.post_metadata.postDate,
        "summary": self.post_card.postCardSummary,
        "readingTime": self.post_metadata.postReadTime
      }
    )

    for metadata in all_metadata:
      if not metadata["title"]:
        return False
      if not metadata["date"]:
        return False
      if not metadata["summary"]:
        return False
      if not metadata["readingTime"]:
        return False

    return True
