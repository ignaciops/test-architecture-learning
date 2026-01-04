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
- [ ] `PlaywrightBrowserAdapter` (implementación)
- [ ] `NavigationScenario` (lógica de navegación)
- [ ] `BlogListingScenario` (lógica de listado)
- [ ] Locators centralizados (`common_locators.py`, `home_page_locators.py`)

### Tests E2E
**Target**: 6-8 tests contra el blog

- [ ] `test_home_page.py` (3 tests)
  - [ ] test_user_can_navigate_to_home
  - [ ] test_home_has_main_navigation
  - [ ] test_home_displays_featured_content
- [ ] `test_blog_listing.py` (2-3 tests)
  - [ ] test_blog_listing_loads
  - [ ] test_blog_displays_post_cards
- [ ] `test_post_display.py` (2 tests)
  - [ ] test_post_page_loads
  - [ ] test_post_displays_content

**Progreso**: 1/8 tests (12.5%)

### Infraestructura
- [ ] Docker Compose setup
- [ ] Allure reporting funcionando
- [ ] Screenshots automáticos en fallos (opcional)
- [ ] GitHub Actions básico (opcional - puede moverse a mes 2)

### Contenido Público
- [ ] Lightning talk presentada (28 enero)
  - Tema: Analogía Git → Crecimiento personal
  - Tu roadmap como ejemplo práctico
  - NO es presentación del roadmap (eso es el blog post)
- [ ] Blog post "Roadmap 2026" publicado
- [ ] Video de talk obtenido (opcional)

---

## ✅ Criterios de Éxito

**Obligatorios** (Must Have):
- [ ] Arquitectura hexagonal básica implementada (ports + adapters + scenarios)
- [ ] Mínimo 6 tests E2E funcionando (75% del target)
- [ ] Allure reports generándose correctamente
- [ ] Lightning talk presentada
- [ ] Blog post publicado
- [ ] Retrospectiva del mes escrita

**Opcionales** (Nice to Have):
- [ ] 8 tests completos (100% del target)
- [ ] Docker Compose optimizado
- [ ] Screenshots automáticos funcionando
- [ ] CI básico en GitHub Actions

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
docker-compose up --build

# Run tests only
docker-compose run tests pytest tests/ -v
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
| Semana 1 (1-7 Ene) | TBD | TBD | 1/8 | Setup inicial |
| Semana 2 (8-14 Ene) | - | - | - | - |
| Semana 3 (15-21 Ene) | - | - | - | - |
| Semana 4 (22-31 Ene) | - | - | - | Cierre + retro |

---

## 🔗 Recursos del Mes

### Libros
- **Python Testing with pytest** (Brian Okken) - Capítulos 1-5
- **Clean Architecture** (Robert Martin) - Capítulos sobre Hexagonal

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
| Python | 3.14+ | Lenguaje base |
| Playwright | 1.48+ | E2E testing |
| Pytest | 8.3+ | Test framework |
| pytest-playwright | latest | Plugin integración |
| Allure-pytest | latest | Reporting |
| Docker | latest | Containerización |

---

## 🐛 Issues Conocidos

- [ ] Docker Compose aún no optimizado
- [ ] CI workflow pendiente (mover a mes 2)
- [ ] Allure screenshots solo manual, no automático

---

## 🔄 Ajustes al Plan Original

| Ajuste | Razón | Impacto |
|--------|-------|---------|
| CI básico → Mes 2 | Priorizar tests y arquitectura | Bajo |
| Target flexible (6-8 tests) | Situación familiar + aprendizaje | Mínimo: 6 tests aceptable |

---

## ➡️ Preparación para Mes 2

### Técnico
- [ ] Refactorizar estructura de tests (crear `tests/e2e/blog/`)
- [ ] Preparar para microservicios FastAPI
- [ ] Investigar Testcontainers

### Documentación
- [ ] Escribir retrospectiva completa
- [ ] Documentar lecciones aprendidas
- [ ] Actualizar métricas finales

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

**Última actualización**: 3 Enero 2026
**Próxima revisión**: 31 Enero 2026