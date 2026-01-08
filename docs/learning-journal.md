# Learning Journal - Test Architecture Roadmap 2026

> Registro cronológico de mi aprendizaje. Cada entrada debe tomar ≤30 min escribir.
>
> **Regla de oro**: Solo escribo si tengo algo valioso que documentar. No forzar entradas diarias.

---

## 2025-12-21 | Hexagonal Architecture - First Contact

**⏱️ Tiempo**: 2h | **📚 Fuente**: Alistair Cockburn + Uncle Bob blogs | **🏷️ Tags**: #architecture #patterns #foundations

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

**⏱️ Tiempo**: 2h | **📚 Fuente**: Playwright Python Docs | **🏷️ Tags**: #playwright #e2e #tools

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

**⏱️ Tiempo**: 2h | **📚 Fuente**: Architecture Patterns with Python | **🏷️ Tags**: #architecture #ddd

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
