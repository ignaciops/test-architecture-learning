class BlogPageLocators:
  """
  Locators específicos para la página Blog.
  Patrón: un archivo por página, una clase por página.

  Siguen la convención de nomenclatura:
  - User camelCase para nombres de variables.
  - Siguen la forma: funciónDeElemento tipoDeElemento

  NO incluye:
    - Estructura de post cards (PostCardLocators)
    - Metadatos genéricos (PostMetadataLocators)
  """

  # Content Section
  blogContentSection = "[data-testid='main-content']"
  blogPageTitle = "[data-testid='blog-page-title']"
  blogPostsList = "[data-testid='blog-posts-list']"

  # Nota: Los post-card individuales dentro de blog-post-list usan PostCardLocators