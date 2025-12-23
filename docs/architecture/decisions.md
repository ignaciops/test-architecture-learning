# Architecture Decision Records (Informal)

> Decisiones arquitectónicas importantes tomadas durante el proyecto.
> Formato simplificado de ADRs.

---

## ADR-001: Hexagonal Architecture Pattern

**Fecha**: 2024-12-21
**Status**: ✅ Accepted
**Decidido por**: Ignacio

### Contexto
Necesito un patrón arquitectónico para el framework de testing que:
- Permita cambiar herramientas sin reescribir lógica
- Escale a medida que agrego más tipos de tests (E2E, API, contracts, etc.)
- Sea mantenible por 12 meses de evolución

### Decisión
Usar **Hexagonal Architecture (Ports & Adapters)** como patrón base.

### Estructura
```
framework/
├── domain/
│   ├── ports/       # Interfaces (contratos)
│   └── scenarios/   # Lógica de negocio
├── adapters/
│   ├── playwright/  # Implementación E2E
│   ├── locators/    # Detalles de UI
│   └── api/         # Implementación API (mes 2)
└── infrastructure/
    └── config.py    # Configuración
```

### Consecuencias

**Positivas**:
- ✅ Scenarios independientes de herramientas
- ✅ Puedo cambiar de Playwright a Selenium sin tocar scenarios
- ✅ Fácil agregar nuevos tipos de adapters (API, GraphQL)
- ✅ Tests más legibles (usan scenarios, no detalles)

**Negativas**:
- ⚠️ Más archivos/carpetas que un enfoque simple
- ⚠️ Curva de aprendizaje inicial
- ⚠️ Puede ser over-engineering para <10 tests

**Mitigación**: Como es un proyecto de 12 meses con múltiples fases, la complejidad inicial se justifica.

### Alternativas Consideradas

1. **Page Object Model (tradicional)**
   - Rechazado: Mezcla "qué" con "cómo"
   - No escala bien con múltiples tipos de tests
   - Ya lo domino

2. **Test scripts planos**
   - Rechazado: No reutilizable
   - Difícil de mantener

### Referencias
- [Hexagonal Architecture - Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture - Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

## ADR-002: Centralized Locators

**Fecha**: 2024-12-22
**Status**: ✅ Accepted

### Contexto
Los selectores de UI (CSS, data-testid, etc.) pueden estar:
- Hardcoded en scenarios
- Hardcoded en adapters
- En archivos separados

### Decisión
Crear archivos de locators centralizados en `framework/adapters/locators/`.

**Estructura**:
```python
# framework/adapters/locators/home_locators.py
class HomePageLocators:
    BLOG_TITLE = '[data-testid="blog-title"]'
    POSTS_LIST = '[data-testid="posts-list"]'
```

**Uso**:
```python
# En el adapter
def get_title(self):
    return self._page.locator(HomePageLocators.BLOG_TITLE).inner_text()
```

### Consecuencias

**Positivas**:
- ✅ Cambio un selector en un solo lugar
- ✅ Fácil ver todos los selectores de una página
- ✅ Scenarios no conocen detalles de UI

**Negativas**:
- ⚠️ Un archivo extra por página

### Alternativas Consideradas
- Hardcoded en adapter: rechazado (duplicación)
- Dentro del scenario: rechazado (viola separación de concerns)

---

<!--
Template para futuras decisiones:

## ADR-XXX: Título de la Decisión

**Fecha**: YYYY-MM-DD
**Status**: 🤔 Proposed | ✅ Accepted | ❌ Rejected | ⚠️ Deprecated

### Contexto
Descripción del problema

### Decisión
Qué decidimos hacer

### Consecuencias
Positivas y negativas

### Alternativas Consideradas
Otras opciones y por qué se rechazaron

---
-->
