class PostPageLocators:
  """
  Locators para la página de posts.

  Siguen la convención de nomenclatura:
  - User camelCase para nombres de variables.
  - Siguen la forma: funciónDeElemento tipoDeElemento

  NO incluye metadatos genéricos (PostMetadataLocators).
  """

  # Post
  postHeaderSection = "[data-testid='post-header']"
  postTitle = "[data-testid='post-title']"
  # Nota: post-meta con post-date, reading-time vienen de PostMetadataLocators
  # Nota: tag-list viene de PostMetadataLocators
  # Nota: summary no tiene data-testid según tu descripción
  postCoverImage = "[data-testid='post-cover-image']"
  postContentSection = "[data-testid='post-content']"

  # Table of Contents
  tableOfContents = "[data-testid='table-of-contents']"

  # Navigation
  postNavigationContainer = "[data-testid='post-navigation']"
  previousPostLink = "[data-testid='previous-post-link']"
  nextPostLink = "[data-testid='next-post-link']"
