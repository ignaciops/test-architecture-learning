# Month 01: Foundations + Hexagonal Architecture

**Período**: Enero 2026
**Status**: 🚧 En progreso
**Talk/Video**: "git init - mi proyecto 2026" (28 enero - DgoTecHub)
**Blog Post**: "Roadmap 2026: Test Architecture"

---

## 🎯 Objetivo del Mes

Construir la base del framework con arquitectura hexagonal básica, usando mi blog (Astro + Keystatic) como primer SUT para pruebas E2E. Presentar públicamente el proyecto de aprendizaje y comprometerse con la comunidad.

---

## 📦 Entregables

### Framework Core
**Arquitectura Hexagonal Básica**

- [x] `BrowserPort` (interface)
- [x] `PlaywrightBrowserAdapter` (implementación)
- [x] `NavigationScenario` (lógica de navegación)
- [x] `BlogListingScenario` (lógica de listado)
- [x] Locators centralizados (`common_locators.py`, `home_page_locators.py`)

### Tests E2E
**Target**: 8 - 10 tests contra el blog

- [x] `test_home_page_loads_correctly.py` (1 test)
  - [x] test_home_displays_all_sections
- [x] `test_blog_listing.py` (3 tests)
  - [x] test_blog_listing_displays
  - [x] test_user_can_navigate_to_specific_post
  - [x] test_all_posts_have_metadata
- [x] `test_featured_post_navigation.py` (1 tests)
  - [x] test_user_can_read_featured_post
- [x] `test_tag_navigation.py` (1 tests, 3 tests con parametrización)
  - [x] test_user_can_filter_posts_by_tag_from_card
- [x] `test_responsive_design.py` (1 test)
  - [x] test_home_page_shows_elements
- [x] `test_mobile_blog_listing.py` (3 tests same tests from `test_blog_listing.py`)
  - [x] test_mobile_blog_listing_displays
  - [x] test_mobile_user_can_navigate_to_specific_post
  - [x] test_mobile_all_posts_have_metadata

**Progreso**: 10/10 tests (100%)
**Nota**: Los tests de `test_mobile_blog_listing.py` son los mismos de `test_blog_listing.py` para probar la navegación en móvil. En meses futuros se implementará parametrización y ejecución sepaada con CI/CD"

### Infraestructura
- [x] Docker Compose setup
  - Dockerfile con Playwright v1.48
  - docker-compose.yml con servicios tests + allure
  - .dockerignore optimizado
  - Allure con historial habilitado
  - Documentación completa de uso
- [x] Allure reporting funcionando
- [x] Screenshots automáticos en fallos (opcional)
- [x] GitHub Actions básico (opcional - puede moverse a mes 2)

### Contenido Público
- [x] Lightning talk presentada (28 enero)
  - Tema: Analogía Git → Crecimiento personal
  - Tu roadmap como ejemplo práctico
  - NO es presentación del roadmap (eso es el blog post)
- [x] Blog post "Roadmap 2026" publicado
- [ ] Video de talk obtenido (opcional)

---

## ✅ Criterios de Éxito

**Obligatorios** (Must Have):
- [x] Arquitectura hexagonal básica implementada (ports + adapters + scenarios)
- [x] Mínimo 6 tests E2E funcionando (75% del target)
- [x] Allure reports generándose correctamente
- [x] Lightning talk presentada
- [x] Blog post publicado
- [x] Retrospectiva del mes escrita

**Opcionales** (Nice to Have):
- [x] 10 tests completos (100% del target)
- [x] Docker Compose optimizado
- [x] Screenshots automáticos funcionando
- [x] CI básico en GitHub Actions
- [x] Service Layer con FakeBrowserAdapter
- [x] 4-6 tests edge-to-edge

---

## 🚀 Quick Start

### Setup
```bash
# Install dependencies
pip install -e .
playwright install --with-deps

# Verify setup
pytest tests/ --collect-only
```

### Run Tests
```bash
# Against production (default)
pytest tests/ -v

# Against local blog (if running)
BLOG_BASE_URL=http://localhost:4321 pytest tests/ -v

# With browser visible
pytest tests/ --headed -v

# Generate Allure report
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

### Docker
```bash
# Build and run
docker compose up --build

# Run tests only
docker compose run tests pytest tests/ -v
```

---

## 📚 Aprendizajes Planeados

### Conceptos Técnicos
1. **Arquitectura Hexagonal (Ports & Adapters)**
   - Separación dominio vs infraestructura
   - Ports como interfaces
   - Adapters como implementaciones
   - Scenarios como lógica de negocio

2. **Playwright Python**
   - Configuración básica
   - Locator strategies (data-testid)
   - Page interactions
   - Auto-waiting

3. **Pytest Avanzado**
   - Fixtures con scope
   - Fixtures dependency injection
   - Markers (smoke, e2e, etc.)

4. **Allure Reporting**
   - Decorators (@allure.feature, @allure.story)
   - Steps dinámicos
   - Attachments (screenshots)

### Habilidades Blandas
- Compromiso público con aprendizaje
- Documentación clara
- Presentación ante comunidad
- Timeboxing y gestión de alcance

---

## 📊 Progreso Semanal

**Última actualización**: 3 Enero 2026

| Semana | Tiempo | Commits | Tests | Notas |
|--------|--------|---------|-------|-------|
| Semana 1 (1-11 Ene) | 16 | 15 | 2/10 | Setup inicial |
| Semana 2 (12-18 Ene) | 6 | 2 | 5/10 | Ports y Adapters mejorados, Adapters completos |
| Semana 3 (19-25 Ene) | ~17 | 15 | 10/10 | Done|
| Semana 4 (26 Ene - 1 Feb) | - | - | - | Cierre + retro |

**Nota**: Semana 1 abarca 11 días ya que Enero inició a mitad de semana. Por tal motivo, semana 4 incluye incluye el domingo 1 de febrero.
---

## 🔗 Recursos del Mes

### Libros
- **Python Testing with pytest** (Brian Okken) - Capítulos 1-5
- **Clean Architecture** (Robert Martin) - Capítulos sobre Hexagonal
- **Architecture Patterns with Python** (Harry Percival, Bob Gregory) - Capítulos 1 - 7

### Documentación Oficial
- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Docs - Fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [Allure Pytest](https://docs.qameta.io/allure-report/)

### Artículos
- Martin Fowler: "Page Object" (para entender qué reemplazamos)
- "Beyond Page Objects" - InfoQ
- "Hexagonal Architecture in Test Automation" - Medium

---

## 📝 Notas de Implementación

### Decisiones Técnicas

**data-testid como estrategia principal**
Todos los elementos interactivos del blog tienen `data-testid` para selectores estables.

Ver: [ADR-002: Selectores - Decisión de nombres](../../docs/architecture/decisions/ADR-002-selectores-decision-de-nombres.md)

**Common Locators separados**
Elementos compartidos (navbar, footer, logo) en `common_locators.py`.

Ver: [ADR-003: Separación Common Locators](../../docs/architecture/decisions/ADR-003-separacion-common-locators.md)

### Stack Técnico

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| Python | 3.12+ | Lenguaje base |
| Playwright | 1.48+ | E2E testing |
| Pytest | 8.3+ | Test framework |
| pytest-playwright | latest | Plugin integración |
| Allure-pytest | latest | Reporting |
| Docker | latest | Containerización |


---

## 🔄 Ajustes al Plan Original

| Ajuste | Razón | Impacto |
|--------|-------|---------|
| CI básico → Mes 2 | Priorizar tests y arquitectura | Bajo |
| Target flexible (8 - 10 tests) | Situación familiar + aprendizaje | Mínimo: 8 tests aceptable |

---

## ➡️ Preparación para Mes 2

### Técnico
- [ ] Refactorizar estructura de tests (crear `tests/e2e/blog/`)
- [ ] Preparar para microservicios FastAPI
- [ ] Investigar Testcontainers

### Documentación
- [x] Escribir retrospectiva completa
- [x] Documentar lecciones aprendidas
- [x] Actualizar métricas finales

### Contenido
- [ ] Obtener video de lightning talk
- [ ] Embedear video en blog post

---

## 🔗 Ver También

- [Roadmap completo](../../months/README.md)
- [Workflows](../../docs/workflows.md)
- [Learning Journal](../../docs/learning-journal.md)
- [Architecture Decisions](../../docs/architecture/decisions/)
- [RETROSPECTIVE.md](RETROSPECTIVE.md) - Se escribirá al final del mes

---

**Última actualización**: 30 Enero 2026
**Próxima revisión**: 31 Enero 2026