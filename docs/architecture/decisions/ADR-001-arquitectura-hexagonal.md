# ADR-001: Patrón de Arquitectura Hexagonal

**Fecha**: 21-12-2025
**Estado**: Aceptado
**Mes**: 01 - Foundations

---
## Contexto
Al iniciar el proyecto de Arquitectura de Pruebas de 12 meses, necesito un patrón arquitectónico que:

- Permita cambiar de herramientas sin reescribir lógica de negocio
- Escale a medida que agrego tipos de tests (E2E, API, contracts, performance, chaos, etc)
- Sea mantenible durante 12 meses de cambio continuo
- Facilite aprendizaje profundo de arquitectura (objetivo explícito del roadmap)

El proyecto evolucionará mes a mes:
- Mes 1: E2E con Playwright
- Mes 2: API testing con HTTPX
- Mes 3: Contract testing con Pact
- Meses 4 - 12: Observability, performance, chaos, security, accessibility, etc.

**Opciones consideradas**
1. **Page Object Model**. Rechazado (mezcla "que" con "cómo" con mala implementación. No escala bien, ya lo domino)
2. **Scripts planos**. Rechazaod (duplicación, no mantenible)
3. **Hexagonal Architecture (Ports & Adapters)**. Elegido

---
## Decision
Adoptar **Hexagonal Architecture (Ports & Adapters)** como patrón base del framework.

## Estructura implementada
```
framework/
├── ports/           # Interfaces (contratos abstractos)
│   ├── browser_port.py
│   └── api_port.py  (mes 2)
├── scenarios/       # Lógica de negocio (independiente de herramientas)
│   ├── navigation_scenario.py
│   └── user_scenario.py
├── adapters/        # Implementaciones concretas
│   ├── locators/    # Detalles de UI
│   ├── playwright/  # Implementación de BrowserPort
│   └── api/         # Implementación de ApiPort (mes 2)
└── infrastructure/  # Config, logging, etc.
    └── config.py
```

### Principios Clave
1. **Ports (Interfaces)**: Definen QUÉ se puede hacer (sin especificar CÓMO)
2. **Scenarios**: Contienen lógica de negocio, solo dependen de Ports
3. **Adapters**: Implementan Ports usando herramientas específicas
4. **Tests**: Usan Scenarios, nunca Adapters directamente

---
## Consecuencias
### Positivas
- Scenarios independientes de herramientas. Cambio de Playwright a Selenium sin tocar lógica
- Reutilización de lógica entre tipos de tests. Un scenario de "login" sirve para E2E y API
- Tests más legibles. Usan lenguaje de negocio (`navigate_to_home()`) vs `page.goto(URL)`)
- Base sólida para meses futuros. Contract testing, observability, etc. encajan naturalmente
- Aprendizaje profundo. Dominar el patrón es el objetivo del roadmap.

### Negativas
- Setup inicial más complejo. Más tiempo en mes 1
- Curva de aprendizaje. Primeras semanas más lentas debido a aprendizaje
- Overhead para tests simples. Un test básico requiere Port, Adapter y Scenario

Mitigación: Es un proyecto de 12 meses donde el objetivo es aprender arquitectura de pruebas.
---
## Ejemplo
### Port (Interface)
```python
# framework/ports/browser_port.py
from abc import ABC, abstractmethod

class BrowserPort(ABC):
    """Interface que define capacidades del navegador"""

    @abstractmethod
    def navigate(self, url: str) -> None:
        pass

    @abstractmethod
    def click(self, locator: str) -> None:
        pass

    @abstractmethod
    def is_visible(self, locator: str) -> bool:
        pass
```

### Adapter (Implementación con Playwright)
```python
# framework/adapters/playwright/browser_adapter.py
from playwright.sync_api import Page
from framework.ports.browser_port import BrowserPort

class PlaywrightAdapter(BrowserPort):
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: str) -> None:
        self.page.locator(locator).click()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()
```

### Scenario (Lógica de Negocio)
```python
# framework/scenarios/navigation_scenario.py
from framework.ports.browser_port import BrowserPort

class NavigationScenario:
    def __init__(self, browser: BrowserPort, base_url: str):
        self.browser = browser
        self.base_url = base_url

    def go_to_home(self) -> None:
        """Navega a la página home"""
        self.browser.navigate(self.base_url)

    def verify_home_loaded(self) -> bool:
        """Verifica que home cargó correctamente"""
        return self.browser.is_visible("[data-testid='site-title']")
```

### Test (Usa Scenario)
```python
# tests/test_home.py
def test_home_page_loads(navigation_scenario):
    # Test solo usa lenguaje de negocio
    navigation_scenario.go_to_home()
    assert navigation_scenario.verify_home_loaded()
```

El test NO conoce que se usa Playwright, ni URLs, ni locators. Solo usa lenguaje de negocio.
---
## Referencias
- [Hexagonal Architecture - Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture - Robert Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
---
**Última revisión**: 03-01-2026