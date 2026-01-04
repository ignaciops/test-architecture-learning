# Arquitectura del Framework de Testing

Este framework implementa el patrón **Hexagonal Architecture (Ports & Adapters)** para maximizar mantenibilidad y facilitar cambio de herramientas.

**Última actualización**: 3 Enero 2026

---

## 🎯 Filosofía

> "El framework debe expresar QUÉ testeamos (lógica de negocio), no CÓMO lo testeamos (herramientas específicas)"

**Principios**:
1. **Lógica de negocio independiente** de herramientas (Playwright, HTTPX, etc.)
2. **Cambiar herramientas sin romper tests** (ej: Playwright → Selenium)
3. **Reutilizar lógica** entre diferentes tipos de tests (E2E, API, mobile)
4. **Testear el framework** sin ejecutar navegadores

---

## 🏗️ Estructura del Framework (Ideal - Objetivo a fin del mes 1)
```
framework/
├── domain/                    # Núcleo - Lógica de negocio
│   ├── ports/                 # Interfaces (contratos)
│   │   ├── browser_port.py    # "Qué puedo hacer con un navegador"
│   │   └── api_port.py        # "Qué puedo hacer con una API"
│   └── scenarios/             # Lógica de negocio (tool-agnostic)
│       ├── navigation_scenario.py
│       └── blog_listing_scenario.py
│
├── adapters/                  # Infraestructura - Implementaciones
│   ├── locators/              # Selectores UI centralizados
│   │   ├── common_locators.py
│   │   └── home_page_locators.py
│   ├── playwright/            # Implementación con Playwright
│   │   └── browser_adapter.py
│   └── api/                   # Implementación con HTTPX
│       └── http_adapter.py
│
└── infrastructure/            # Configuración y utilidades
    ├── config.py
    └── logging_config.py
```

---

## 🔌 Capa 1: Ports (Interfaces)

**Propósito**: Definir **QUÉ** se puede hacer, no **CÓMO**.

**Ejemplo**: `browser_port.py`
```python
from abc import ABC, abstractmethod

class BrowserPort(ABC):
    """Interface que define capacidades de un navegador"""

    @abstractmethod
    def navigate_to(self, url: str) -> None:
        """Navegar a una URL"""
        pass

    @abstractmethod
    def click(self, locator: str) -> None:
        """Hacer clic en un elemento"""
        pass

    @abstractmethod
    def get_text(self, locator: str) -> str:
        """Obtener texto de un elemento"""
        pass
```

**Características**:
- ✅ Abstracto (ABC)
- ✅ Sin dependencias de Playwright, Selenium, etc.
- ✅ Representa capacidades del negocio

---

## 🔧 Capa 2: Adapters (Implementaciones)

**Propósito**: Implementar ports usando herramientas específicas.

**Ejemplo**: `playwright_adapter.py`
```python
from playwright.sync_api import Page
from framework.domain.ports.browser_port import BrowserPort

class PlaywrightBrowserAdapter(BrowserPort):
    """Implementación de BrowserPort usando Playwright"""

    def __init__(self, page: Page):
        self._page = page

    def navigate_to(self, url: str) -> None:
        self._page.goto(url)

    def click(self, locator: str) -> None:
        self._page.locator(locator).click()

    def get_text(self, locator: str) -> str:
        return self._page.locator(locator).inner_text()
```

**Características**:
- ✅ Implementa el port
- ✅ Depende de Playwright (herramienta específica)
- ✅ Traduce llamadas del port a API de Playwright

---

## 🎬 Capa 3: Scenarios (Lógica de Negocio)

**Propósito**: Orquestar acciones de negocio usando ports.

**Ejemplo**: `navigation_scenario.py`
```python
from framework.domain.ports.browser_port import BrowserPort
from framework.adapters.locators.common_locators import CommonLocators

class NavigationScenario:
    """Lógica de navegación del sitio"""

    def __init__(self, browser: BrowserPort):
        self._browser = browser  # Depende del PORT, no del adapter

    def go_to_home(self, base_url: str) -> None:
        """Usuario navega al home"""
        self._browser.navigate_to(base_url)

    def go_to_blog(self) -> None:
        """Usuario navega al blog desde cualquier página"""
        self._browser.click(CommonLocators.NAV_BLOG_LINK)
```

**Características**:
- ✅ Depende del **port** (interface), no del adapter
- ✅ Expresa lógica de negocio ("ir al blog")
- ✅ No sabe si usa Playwright, Selenium, o API

---

## 🧪 Capa 4: Tests

**Propósito**: Ejercitar scenarios con datos específicos.

**Ejemplo**: `test_blog_navigation.py`
```python
import pytest
from framework.domain.scenarios.navigation_scenario import NavigationScenario

def test_user_can_navigate_to_blog(navigation_scenario: NavigationScenario, config):
    """Usuario puede navegar del home al blog"""
    # Arrange
    navigation_scenario.go_to_home(config.BLOG_BASE_URL)

    # Act
    navigation_scenario.go_to_blog()

    # Assert
    # ... verificaciones ...
```

**Características**:
- ✅ Depende de **scenarios**, no de adapters
- ✅ Expresa casos de uso de negocio
- ✅ Herramienta subyacente es transparente

---

## 🔄 Flujo de Dependencias
```
Tests
  ↓ depende de
Scenarios (lógica de negocio)
  ↓ depende de
Ports (interfaces)
  ↑ implementado por
Adapters (Playwright, HTTPX, etc.)
```

**Regla de oro**: Las dependencias apuntan **hacia adentro** (hacia la lógica de negocio).

---

## 🎯 Beneficios

### 1. Cambio de Herramientas sin Romper Tests

**Antes (Page Objects tradicional)**:
```python
# Si cambias de Playwright a Selenium, rompes TODO
page.locator("#blog-link").click()  # Código Playwright everywhere
```

**Después (Hexagonal)**:
```python
# Scenarios NO cambian - solo creas nuevo adapter
browser.click(CommonLocators.NAV_BLOG_LINK)  # Interface estable
```

### 2. Reutilización de Lógica

**Mismo scenario, múltiples adapters**:
```python
# E2E con Playwright
browser = PlaywrightBrowserAdapter(page)
nav = NavigationScenario(browser)

# Mobile con Appium (futuro)
browser = AppiumBrowserAdapter(driver)
nav = NavigationScenario(browser)  # Misma lógica!
```

### 3. Tests del Framework sin UI

**Mockear el port para tests rápidos**:
```python
class MockBrowser(BrowserPort):
    def click(self, locator: str):
        self.clicked.append(locator)  # Solo trackear llamadas

# Test del scenario sin navegador real
mock = MockBrowser()
nav = NavigationScenario(mock)
nav.go_to_blog()
assert CommonLocators.NAV_BLOG_LINK in mock.clicked
```

---

## 📋 Locators Centralizados

**Estrategia**: Separar locators de lógica.
```
adapters/locators/
├── common_locators.py      # Elementos compartidos (navbar, footer)
└── home_page_locators.py   # Elementos específicos de home
```

**Ejemplo**: `common_locators.py`
```python
class CommonLocators:
    """Locators de elementos compartidos en todo el sitio"""

    # Navbar
    NAV_LOGO = '[data-testid="nav-logo"]'
    NAV_HOME_LINK = '[data-testid="nav-home"]'
    NAV_BLOG_LINK = '[data-testid="nav-blog"]'

```

**Ver**: [ADR-003: Separación Common Locators](decisions/ADR-003-separacion-common-locators.md)

---

## 🚀 Agregar Nuevas Capacidades

### Nuevo Port + Adapter

**1. Definir el port** (`domain/ports/storage_port.py`):
```python
class StoragePort(ABC):
    @abstractmethod
    def save(self, key: str, value: str) -> None:
        pass
```

**2. Implementar adapter** (`adapters/redis/redis_adapter.py`):
```python
class RedisStorageAdapter(StoragePort):
    def save(self, key: str, value: str) -> None:
        self._redis.set(key, value)
```

**3. Usar en scenario**:
```python
class DataScenario:
    def __init__(self, storage: StoragePort):  # Port!
        self._storage = storage
```

### Nuevo Scenario

**1. Crear archivo** (`domain/scenarios/checkout_scenario.py`):
```python
class CheckoutScenario:
    def __init__(self, browser: BrowserPort, api: APIPort):
        self._browser = browser
        self._api = api

    def complete_purchase(self, product_id: str):
        # Lógica de negocio aquí
        pass
```

**2. Usar en tests**:
```python
def test_user_can_checkout(checkout_scenario):
    checkout_scenario.complete_purchase("PROD-123")
```

---

## 📚 Decisiones Arquitectónicas

Para entender **por qué** se tomaron decisiones específicas:

👉 [Ver ADRs completos](decisions/README.md)

**ADRs actuales**:
- ADR-001: Por qué Hexagonal Architecture
- ADR-002: Convención de nombres de locators
- ADR-003: Separación de common locators

---

## 🎓 Aprender Más

### Recursos sobre Hexagonal Architecture

**Artículos**:
- [Alistair Cockburn - Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- ["Clean Architecture" by Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

**Videos**:
- "Beyond Page Objects" - Angie Jones
- "Hexagonal Architecture in Testing" - varios en YouTube

### Sobre este Framework

- [Learning Journal](../learning-journal.md) - Aprendizajes documentados
- [Workflows](../workflows.md) - Cómo trabajamos
- [Roadmap](../../months/README.md) - Plan de 12 meses

---

**Última actualización**: 3 Enero 2026
**Próxima revisión**: 31 Enero 2026
```
