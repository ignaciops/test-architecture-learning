# ADR-003: Separación de Selectores Comunes

**Fecha**: 03-01-2026
**Estado**: Aceptado
**Mes**: 01 - Foundations
---
## Contexto

Al implementar locators centralizados (ADR-002), surge la pregunta de cómo organizar elementos que aparecen en múltiples páginas.

**Escenario específico**: Elementos como logo del blog, navbar y footer aparecen en TODAS las páginas.

**Opciones:**
1. **Duplicar en cara archivo de página**
- `home_page_locators.py` tiene `siteLogo`
   - `blog_page_locators.py` tiene `siteLogo` (duplicado)
   - `post_page_locators.py` tiene `siteLogo` (duplicado)

2. **Centralizar elementos compartidos**
   - `common_locators.py` tiene `siteLogo`
   - Los archivos de página solo tienen elementos específicos

---

## Decisión

Crear **`common_locators.py`** para elementos que aparecen en 2 o más páginas con el mismo propósito.

### Regla de Decisión

Un locator va a `common_locators.py` si cumple **AMBOS** criterios:

1. Aparece en **2 o más páginas**
2. Tiene el **mismo propósito** en todas ellas

### Estructura Implementada
```
framework/adapters/locators/
├── __init__.py
├── common_locators.py       # Navbar, footer, logo
├── home_page_locators.py    # Hero, featured posts (solo en home)
├── blog_page_locators.py    # Post list, (solo en blog)
└── post_page_locators.py    # Post content, metadata (solo en posts)
```

---

## Consecuencias

### Positivas

- **Single Source of Truth**: Cambio el selector del logo en UN solo lugar
- **Fácil identificar qué es compartido**: `common_locators.py` documenta elementos globales
- **Tests más expresivos**: Se ve claramente cuando usas elementos globales vs específicos
- **Escalabilidad**: Nuevas páginas reutilizan locators sin duplicar

### Negativas

- **Imports adicionales**: Tests necesitan importar 2+ archivos de locators
- **Decisión inicial**: Al crear un locator, debo evaluar si es común o específico

**Mitigación**: La inversión de tiempo en decidir se recupera cada vez que cambio un selector compartido.

---

## Ejemplos de Clasificación

### Elementos en `common_locators.py`

| Elemento | Justificación |
|----------|---------------|
| `siteLogo` | Aparece en todas las páginas, siempre link a home |
| `siteTitle` | Aparece en todas las páginas, mismo texto |
| `navbarContainer` | Navbar presente en todas las páginas |
| `navbarBlogLink` | Link a blog en navbar (todas las páginas) |
| `footerContainer` | Footer en todas las páginas |

### Elementos en `home_page_locators.py`

| Elemento | Justificación |
|----------|---------------|
| `heroTitle` | Solo aparece en home |
| `heroSubtitle` | Solo aparece en home |
| `featuredSection` | Solo aparece en home |
| `featuredPostCard` | Solo aparece en home |

### Elementos en `blog_page_locators.py`

| Elemento | Justificación |
|----------|---------------|
| `postList` | Solo aparece en página de blog |
| `postCard` | Cards de posts (aunque posts también los tienen, el contexto es diferente) |
| `paginationControls` | Solo en listado de blog |

---

## Implementación

### `common_locators.py`
```python
class CommonLocators:
    """
    Elementos que aparecen en 2+ páginas con el mismo propósito.
    Convención: funcionDelElemento + tipoDeElemento (camelCase)
    """
    # Site
    siteLogo = "[data-testid='site-logo']"
    siteTitle = "[data-testid='site-title']"

    # Navbar
    navbarContainer = "[data-testid='main-navigation']"
    navbarBlogLink = "[data-testid='nav-link-blog']"
    navbarProyectosLink = "[data-testid='nav-link-portfolio']"
    navbarAcercaLink = "[data-testid='nav-link-about']"
    navbarThemeToggle = "[data-testid='theme-toggle-button']"

    # Footer
    footerContainer = "[data-testid='site-footer']"
    footerCopyright = "[data-testid='footer-copyright']"
```

### `home_page_locators.py`
```python
class HomePageLocators:
    """
    Elementos específicos de la página Home.
    NO incluye navbar, footer, logo (están en CommonLocators).
    """
    # Hero Section
    heroTitle = "[data-testid='hero-title']"
    heroSubtitle = "[data-testid='hero-subtitle']"
    heroCtaButton = "[data-testid='hero-cta']"

    # Featured Posts
    featuredSection = "[data-testid='featured-section']"
    featuredPostCard = "[data-testid='featured-post']"
    featuredPostTitle = "[data-testid='featured-post-title']"
```

---

## Uso en Tests

### Correcto
```python
from framework.adapters.locators.common_locators import CommonLocators
from framework.adapters.locators.home_page_locators import HomePageLocators

def test_home_page_loads(navigation_scenario):
    navigation_scenario.go_to_home()

    # Elemento común (navbar en todas las páginas)
    assert navigation_scenario.browser.is_visible(CommonLocators.siteLogo)

    # Elemento específico de Home
    assert navigation_scenario.browser.is_visible(HomePageLocators.heroTitle)
```

### Incorrecto
```python
from framework.adapters.locators.home_page_locators import HomePageLocators

def test_home_page_loads(navigation_scenario):
    navigation_scenario.go_to_home()

    # siteLogo debería venir de CommonLocators, no de HomePageLocators
    assert navigation_scenario.browser.is_visible(HomePageLocators.siteLogo)
```

---

## Casos Especiales

### ¿Qué pasa si un elemento aparece en 2 páginas pero con propósito diferente?

**No va a CommonLocators**. Ejemplo:
```python
# home_page_locators.py
featuredPostCard = "[data-testid='featured-post']"  # En contexto de "destacados"

# blog_page_locators.py
postCard = "[data-testid='post-card']"  # En contexto de "listado completo"
```

Aunque ambos son "cards de posts", el contexto es diferente, por lo que cada uno está en su archivo específico.

---

## Notas

Este ADR complementa ADR-002 (convención de nomenclatura). Juntos definen la estrategia completa de locators:

- **ADR-002**: Cómo nombrar locators (camelCase, funcion + tipo)
- **ADR-003**: Dónde ubicar locators (common vs page-specific)

---

**Última revisión**: 03-01-2026