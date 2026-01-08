"""
Locators para la página Home de mi blog.
Patrón: un archivo por página, una clase por página.
"""

class HomePageLocators:
  """
  Locators de elementos en la página Home.
  Siguen la convención de nomenclatura:
  - User camelCase para nombres de variables.
  - Siguen la forma: funciónDeElemento tipoDeElemento

  NO incluye:
    - Navbar, footer (CommonLocators)
    - Metadatos genéricos (PostMetadataLocators)
    - Estructura de post cards regulares (PostCardLocators)
  """

  # Hero Section
  heroSection = "[data-testid='hero-section']"
  heroImage = "[data-testid='hero-background-image']"
  heroDescription = "[data-testid='hero-description']"

  # Featured Posts Section
  feauturedPostCard = "[data-testid='featured-post']"
  featuredPostImage = "[data-testid='featured-post-image']"
  featuredPostTitle = "[data-testid='featured-post-title']"
  featuredPostSummary = "[data-testid='featured-post-summary']"
  # Nota: featuredPost usa post-meta, post-date, reading-time, tag-list (PostMetadataLocators)

  # Recents Posts Section. Para los locators de los posts individuales, usa PostCardLocators
  recentPostsSection = "[data-testid='recent-posts-section']"
  recentPostsList = "[data-testid='recent-posts-list']"