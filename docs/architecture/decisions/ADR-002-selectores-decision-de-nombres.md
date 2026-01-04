# ADR-002: Selectores. Decisión de nomenclatura

**Fecha**: 22-12-2025
**Estado**: Aceptado
**Mes**: 01 - Foundations
---
## Contexto
Al implementar locators(selectores) centralizados (parte de la arquitectura hexagonal), necesito definir una convención de nomenclatura consistente para los locators de UI.

Consideraciones:
- El blog usa Astro + Keystatic
- Python usa snake_case por convención (PEP 8)
- Quiero consistencia entre frontend y tests
- Los nombres deben ser autoexplicativos

**Opciones consideradas**:
1. **snake_case**: `navbar_blog_link`
2. **SCERAMING_SNAKE_CASE**: `NAVBAR_BLOG_LINK`
3. **camelCase**: `navbarBlogLink`

---
## Decisión

Usar **camelCase** para nombers de locators, siguiendo el patrón:
**`funcionDelElemento + tipoDeElemento`**

### Ejemplos
```python
class CommonLocators:
    """
    Locators comunes a múltiples páginas.
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
    footerSocialLinks = "[data-testid='footer-social-links']"
    footerCopyright = "[data-testid='footer-copyright']"
```

### Anatomía del Nombre
```
navbarBlogLink
│      │    │
│      │    └─── Tipo de elemento (Link, Button, Container, Input, etc.)
│      └──────── Función o identificador del elemento
└─────────────── Componente o sección (navbar, footer, hero, etc.)
```

## Consecuencias

### Positivas

- **Consistencia con frontend**: camelCase es estándar en JavaScript/TypeScript (Astro/React)
- **Autoexplicativos**: `navbarBlogLink` se lee como "navbar blog link"
- **Evita conflictos**: No choca con snake_case de funciones Python
- **Fácil de escanear**: Diferenciación visual clara entre locators y código Python

### Negativas

- **Rompe PEP 8**: Python recomienda snake_case para variables
- **Inconsistencia interna**: El resto del código Python usa snake_case

**Justificación**: Los locators son referencias a elementos de UI (frontend), no lógica Python. Tratarlos como "bridge" hacia el frontend justifica usar su convención.

---
## Comparación de Estilos
```python
# camelCase (elegido)
navbarBlogLink = "[data-testid='nav-link-blog']"

# snake_case
navbar_blog_link = "[data-testid='nav-link-blog']"

# SCREAMING_SNAKE_CASE
NAVBAR_BLOG_LINK = "[data-testid='nav-link-blog']"
```

**Decisión**: camelCase gana por consistencia con el SUT (blog en Astro/React).

---
## Reglas Adicionales

### 1. Agrupación con Comentarios
```python
class HomePageLocators:
    # Hero Section
    heroTitle = "[data-testid='hero-title']"
    heroSubtitle = "[data-testid='hero-subtitle']"
    heroCtaButton = "[data-testid='hero-cta']"

    # Featured Posts
    featuredSection = "[data-testid='featured-section']"
    featuredPostCard = "[data-testid='featured-post']"
```

### 2. Métodos para Locators Dinámicos
```python
class BlogPageLocators:
    # Estáticos
    postList = "[data-testid='post-list']"

    # Dinámicos (cuando necesites parámetros)
    @staticmethod
    def postCardById(post_id: str) -> str:
        return f"[data-testid='post-{post_id}']"
```

### 3. data-testid como Estrategia Principal

La mayoría de los elementos interactivos tienen `data-testid`. Algunos elementos se dejaron sin `data-testid` a propósito para práctica de uso de locators.
---
## Uso en Código

### Adapter
```python
from framework.adapters.locators.common_locators import CommonLocators

class PlaywrightAdapter(BrowserPort):
    def click_blog_link(self) -> None:
        self.page.locator(CommonLocators.navbarBlogLink).click()

    def verify_logo_visible(self) -> bool:
        return self.page.locator(CommonLocators.siteLogo).is_visible()
```

### Scenario (no conoce locators directamente)
```python
class NavigationScenario:
    def go_to_blog(self) -> None:
        """Navega a la sección de blog"""
        self.browser.click_blog_link()  # Abstracción
```
---
## Notas

Esta convención aplica SOLO a archivos de locators. El resto del código Python sigue PEP 8 (snake_case para variables, funciones, métodos).

---

**Última revisión**: 03-01-2026