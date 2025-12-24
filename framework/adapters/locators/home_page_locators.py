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
  """
  # Header
  siteTitle = "[data-testid='site-logo']"
  navigationBlogButton = "[data-testid='nav-link-blog']"
  navigationProyectosButton = "[data-testid='nav-link-portfolio']"
  navigationAcercaButton = "[data-testid='nav-link-about']"
  themeToggleButton = "[data-testid='theme-toggle-button']"

  # Hero Section
  heroSection = "[data-testid='hero-section']"
  heroImage = "[data-testid='hero-background-image']"
  heroDescription = "[data-testid='hero-description']"