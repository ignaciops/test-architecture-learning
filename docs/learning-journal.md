# Learning Journal - Test Architecture Roadmap 2026

> Registro cronológico de mi aprendizaje. Cada entrada debe tomar ≤30 min escribir.
>
> **Regla de oro**: Solo escribo si tengo algo valioso que documentar. No forzar entradas diarias.

---

## 2026-01-19 | Parametrización de tests y la importancia de ser específico con selectors.

**⏱️ Tiempo**: 3 hrs | **📚 Fuente**: Sesión de Código y Debugging real | **🏷️ Tags**: #playwright #locators #debugging #pytest #parameters

### 💡 Main Takeaway
Sobre parametrización:
> "Validar el mismo flujo con múltiples inputs sin duplicar código ahorra tiempo"

Sobre selectores:
> "Los selectores CSS con `^=` (starts-with) pueden ser demasiado amplios.
> Especificidad de contexto (parent > child) previene matches ambiguos."

### 🔑 Conceptos clave
- **Mejor cobertura**: Usar parametrización da cobertura más amplia (3 posts vs 1)
- **Falla clara**: Cada índice genera un test independiente, sé exactamente cuál falla y por qué.
- **Selector amplio**: `[data-testid^='tag-']` coincide con CUALQUIER elemento tag-*
- **Selector específico**: `[data-testid='post-card'] [data-testid='tag-list']`
  establece jerarquía clara
- **Debugging con Allure**: Los attachments de parámetros revelaron que
  todos los tags venían concatenados en un string

### 🎯 Aplicación inmediata
Sobre parametrización:
- Test case `test_user_can_filter_posts_by_tag_from_card` usa índices 0, 2, 4.
- Solo se agrega `@pytest.mark.parametrize("post_index", [0, 2, 4])`
Sobre selectores:
- Cambié `postTagList` a selector con contexto explícito
- Ahora `get_all_texts_from_nested_parent()` funciona correctamente
- Tests de parametrización pasando (índices 0, 2, 4)

### 🐛 Debugging Process
1. Test fallaba con tags concatenados
2. Revisé Allure attachment → "python testing docker" en un string
3. Inspeccioné locator → demasiado amplio
4. Agregué contexto de parent → solucionado

### ➡️ Next
- Buscar otros locators que usen `^=` o `*=` y aplicar mismo principio.

---

## 2026-01-19 | Docker Integration & Allure Screenshots

**⏱️ Tiempo**: ~2 hrs | **📚 Fuente**: Implementación práctica | **🏷️ Tags**: #docker #allure #infrastructure

### 💡 Main Takeaway
> "Registros históricos disponibles desde homelab. Hasta ahora homelab va sobrado para el framework de pruebas."

### 🔑 Conceptos clave
- **Pytest hooks timing**: `pytest_runtest_makereport` captura screenshots ANTES del teardown
- **Docker layer caching**: Orden de COPY optimiza rebuilds (dependencias → código)
- **Version pinning**: playwright==1.57.0 sincronizado entre local y Docker. python>=3.12 para compatibilidad.
- **Allure history**: KEEP_HISTORY=1 acumula resultados para análisis de tendencias

### 🎯 Aplicación inmediata
**Hook de screenshots:**
```python
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_bytes = page.screenshot()
            allure.attach(screenshot_bytes, ...)
```

**Docker build optimization:**
- COPY pyproject.toml primero (cachea si no cambia)
- COPY código después (cambia más seguido)
- Resultado: Rebuilds en <5s si solo cambio tests

### ➡️ Next
- 1 test adicional (navigation flow)
- Actualizar documentación del mes

---
## 2026-01-18 | Service Layer y Edge-to-Edge Testing
⏱️ Tiempo: 6 hrs (Fue sesión de estudio + código) | 📚 Fuente: Architecture Patterns with Python (Cap 4) | 🏷️ Tags: #service-layer #edge-to-edge #fake-adapters #hexagonal-architecture

💡 Main Takeaway

"Mi framework de testing ES software y necesita sus propios tests. Edge-to-edge tests con fake adapters prueban la lógica del framework sin infraestructura real, permitiendo feedback loops ultra-rápidos y mejor cobertura de edge cases."

🔑 Conceptos clave
Service Layer

Orquestación de lógica de negocio separada de infraestructura
Mayor testabilidad mediante funciones con responsabilidad única
Permite que API handlers solo sirvan sin preocuparse de formateo/validación

Edge-to-Edge vs E2E Tests

Edge-to-edge: Domain → Repository fake, muchos tests, milisegundos, todos los edge cases
E2E: API → DB real, pocos tests, segundos, solo happy paths
No son "tests de validación", son tests del framework mismo

Fake Adapters

Implementación del Port que simula estado en memoria (DOM, DB, API)
NO contienen lógica de validación (eso va en Scenarios)
Permiten probar Scenarios sin levantar infraestructura real
Fixtures configuran diferentes estados: complete, incomplete, empty


🎯 Aplicación inmediata
En BlogListingScenario:
```python
# Scenario depende del Port, no del Adapter concreto
class BlogListingScenario:
    def __init__(self, browser: BrowserPort):  # ← Port, no PlaywrightAdapter
        self.browser = browser

    def get_post_metadata(self, index: int) -> dict:
        # Usa métodos del Port
        all_posts = self.browser.get_structured_data(...)

        # VALIDACIÓN aquí (responsabilidad del Scenario)
        if not all_posts:
            raise IndexError("No hay posts disponibles")

        if index >= len(all_posts):
            raise IndexError(f"Índice {index} fuera del rango")

        # Más validaciones de metadatos completos...
        return all_posts[index]
```
Plan semana 3 (Edge-to-edge con fake):

FakeBrowserAdapter con fixtures configurables
Tests rápidos de edge cases (índices fuera de rango, metadatos incompletos)
Probar lógica del Scenario sin levantar browser


❓ Dudas pendientes
Para Mes 3 (Contract Testing):

¿Qué sería el "fake" en Pact consumer/provider tests?
¿Cómo aplicar edge-to-edge con contratos entre microservices?
¿Probar edge cases de contratos sin levantar servicios reales?

Para Mes 2 (Microservices):

¿Usar FakeBrowserAdapter + FakeAPIAdapter en paralelo?
¿Cómo manejar fixtures complejos con múltiples SUTs?


➡️ Next
Semana 3 - Prioridad 1:

Implementar FakeBrowserAdapter básico
Crear 3 fixtures: fake_browser_with_complete_posts, fake_browser_with_incomplete_metadata, fake_browser_empty
Escribir 4-6 tests edge-to-edge del BlogListingScenario

Semana 3 - Lectura:

Architecture Patterns Cap 5-7 (Unit of Work, Aggregates)
Buscar más ejemplos de in-memory repositories aplicados a testing

---

## 2025-12-21 | Hexagonal Architecture - First Contact

**⏱️ Tiempo**: 2 hrs | **📚 Fuente**: Alistair Cockburn + Uncle Bob blogs | **🏷️ Tags**: #architecture #patterns #foundations

### 💡 Main Takeaway
> "La arquitectura hexagonal separa QUÉ testear (scenarios/lógica) del CÓMO testearlo (adapters/herramientas). Los ports son el contrato entre ambos."

### 🔑 Conceptos clave
- **Dependency Rule**: Las dependencias apuntan hacia adentro (lógica → interfaces, no lógica → implementaciones)
- **Ports**: Interfaces abstractas (como TypeScript interfaces) de qué se puede hacer.
- **Adapters**: Implementaciones concretas de los ports. Ejemplo, SeleniumAdapter, PlaywrightAdapter, APIAdapter.
- **Scenarios**: Lógica de negocio que depende de ports, no de adapters

### 🎯 Aplicación inmediata
Para enero implementaré:
```
BrowserPort (interface)
    ↑ implementado por
PlaywrightBrowserAdapter
    ↑ usado por
NavigationScenario (lógica)
    ↑ usado por
Tests
```

### ❓ Dudas pendientes
- ¿Cómo inyectar múltiples ports a un scenario? (ej: BrowserPort + APIPort)
- ¿Los adapters deberían tener tests propios o solo los scenarios?

### ➡️ Next
Leer sobre Dependency Injection en Python para entender mejor las fixtures de pytest.

---

## 2025-12-22 | Playwright Auto-waiting

**⏱️ Tiempo**: 2 hrs | **📚 Fuente**: Playwright Python Docs | **🏷️ Tags**: #playwright #e2e #tools

### 💡 Main Takeaway
> "Nunca usar time.sleep() en tests de Playwright. El auto-waiting espera que el elemento exista + sea visible + sea estable. Si el test falla por timing, el problema es el locator, no la espera."

### 🔑 Conceptos clave
- **Auto-waiting conditions**: Existe en DOM + Visible + Estable + Enabled (para clicks)
- **Locator strategies** (de mejor a peor):
  1. ✅ `get_by_test_id()` - Explícito, no cambia con refactors. Preferible para QA
  2. ✅ `get_by_role()` - Semántico, bueno para a11y. Preferible en general.
  3. ⚠️ `get_by_text()` - Frágil si cambia wording
  4. ❌ `.locator(css)` - Último recurso
- **Chaining**: `.first`, `.last`, `.nth()`, `.filter()`

### 🎯 Aplicación inmediata
- Ya agregué `data-testid` a todos los componentes de mi blog
- En el adapter usaré: `page.get_by_test_id(locator)` donde `locator` viene de `HomePageLocators.BLOG_TITLE`
- El scenario no sabe que uso test-id, solo llama `browser.click("blog-title")`

### ❓ Dudas pendientes
- ¿Soft assertions van en el adapter o en el scenario?

### ➡️ Next
Allure reporting: cómo agregar steps, screenshots automáticos en fallos, y categorización.

---
## 2026-01-06 | Domain Driven Design

**⏱️ Tiempo**: 2 hrs | **📚 Fuente**: Architecture Patterns with Python | **🏷️ Tags**: #architecture #ddd

### 💡 Main Takeaway
> "Los sistemas de software tienden al caos"

### 🔑 Conceptos clave
- Sistemas de software caóticos se caracterizan por funciones que no están claramente separadas en cuanto a responsabilidades.
- Encapsular el comportamiento mediante el uso de abstracciones es una herramienta poderosa para crear código más expresivo, más testeable y más fácil de mantener.
- El modelo de dominio es el mapa mental que los dueños de negocios tienen de su negocio.

### 🎯 Aplicación inmediata
Una arquitectura hexagonal es una "forma" de aplicar Domain Driven Design. Se logra la separación del dominio de negocio a nivel software. Donde se aplica el principio de inversión de dependencia.

La aplicación de DDD se verá reflejada en que los métodos del código van a reflejar el lenguaje del negocio de pruebas (acciones y expectativas), no los detalles técnicos de la herramienta usada.

Ejemplos:
- "navigate_to_blog" (no "click_blog_link")
- "verify_post_is_visible" (no "assert_element_exists")

### ❓ Dudas pendientes
N/A

### ➡️ Next


---

<!--
Template para futuras entradas:

## YYYY-MM-DD | Título Descriptivo

**⏱️ Tiempo**: Xh | **📚 Fuente**: [recurso] | **🏷️ Tags**: #tag1 #tag2

### 💡 Main Takeaway
> "Una frase que resume lo más importante"

### 🔑 Conceptos clave
- Concepto 1
- Concepto 2

### 🎯 Aplicación inmediata
Cómo lo uso en mi proyecto

### ❓ Dudas pendientes
Preguntas que aún tengo

### ➡️ Next
Siguiente paso de aprendizaje

---
-->
