"""
Locators comunes para el blog & portfolio ignaciops.dev
"""

class CommonLocators:
  """
  Locators comunes a múltiples páginas.
  Siguen la convención de nomenclatura:
  - User camelCase para nombres de variables.
  - Siguen la forma: funciónDeElemento tipoDeElemento
  """
  # Site Logo
  siteLogo = "[data-testid='site-logo']"

  # Navbar
  navbarContainer = "[data-testid='main-navigation']"
  navbarBlogLink = "[data-testid='nav-link-blog']"
  navbarProyectosLink = "[data-testid='nav-link-portfolio']"
  navbarAcercaLink = "[data-testid='nav-link-about']"
  navbarThemeToggle = "[data-testid='theme-toggle-button']"

  # Footer
  footerContainer = "[data-testid='site-footer']"
  footerCopyrightText = "[data-testid='site-footer'] p"
  footerGithubLink = "[aria-label='GitHub']"
  footerLinkedinLink = "[aria-label='LinkedIn']"
  footerTwitterLink = "[aria-label='X (Twitter)']"