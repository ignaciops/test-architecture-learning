# Documentación del Proyecto

Índice y guía de navegación para toda la documentación de **Test Architecture Learning 2026**.

---

## 📁 Estructura
```
docs/
├── README.md                    # Este archivo (índice)
├── learning-journal.md          # Diario de aprendizaje
├── scratch.md                   # Notas rápidas (se purga mensualmente)
├── workflows.md                 # Ritmos y procesos de trabajo
├── architecture/
│   ├── README.md                # Overview de arquitectura hexagonal
│   └── decisions/               # Architecture Decision Records (ADRs)
│       ├── template.md
│       └── ADR-XXX-*.md
└── resources/
    └── useful-links.md          # Enlaces útiles, cheatsheets
```

---

## 📖 Guías de Uso

### `learning-journal.md`
**Propósito**: Diario cronológico de aprendizaje con estructura definida por entrada.

**Cuándo escribir**:
- Cuando estudio un tema nuevo (libros, cursos, videos)
- Después de resolver un problema complejo
- **Solo si tengo algo valioso que documentar** (no forzar entradas diarias)
- Tiempo: **≤30 min por entrada**

**Estructura de cada entrada**:
```markdown
## YYYY-MM-DD | Título Descriptivo

**⏱️ Tiempo**: Xh | **📚 Fuente**: [recurso] | **🏷️ Tags**: #tag1 #tag2

### 💡 Main Takeaway
> "Una frase que resume lo más importante"

### 🔑 Conceptos clave
- Concepto 1 explicado brevemente
- Concepto 2 explicado brevemente

### 🎯 Aplicación inmediata
Cómo lo usarás en tu proyecto

### ❓ Dudas pendientes
Preguntas que aún tienes

### ➡️ Next
Siguiente paso de aprendizaje
```

**Ejemplo real**:
```markdown
## 2025-12-21 | Hexagonal Architecture - First Contact

**⏱️ Tiempo**: 2h | **📚 Fuente**: Alistair Cockburn + Uncle Bob | **🏷️ Tags**: #architecture #patterns

### 💡 Main Takeaway
> "La arquitectura hexagonal separa QUÉ testear (scenarios/lógica)
> del CÓMO testearlo (adapters/herramientas)."

### 🔑 Conceptos clave
- Dependency Rule: dependencias apuntan hacia adentro
- Ports: interfaces abstractas de qué se puede hacer
- Adapters: implementaciones concretas (PlaywrightAdapter, etc.)
- Scenarios: lógica de negocio que depende de ports

### 🎯 Aplicación inmediata
BrowserPort → PlaywrightBrowserAdapter → NavigationScenario → Tests

### ❓ Dudas pendientes
- ¿Cómo inyectar múltiples ports a un scenario?
- ¿Los adapters deberían tener tests propios?

### ➡️ Next
Dependency Injection en Python + pytest fixtures
```

**Regla de oro**: Solo escribo si aprendí algo que vale la pena recordar después.
---

### `scratch.md`
**Propósito**: Notas ultra-rápidas sin estructura. Pensamiento en voz alta.

**Cuándo escribir**:
- Durante coding sessions (bugs, ideas, TODOs)
- Notas tipo "post-it" para no olvidar algo
- Patrones o reglas que descubro
- **Cualquier cosa - sin filtro, sin formato**
- Tiempo: **1-5 min, muchas veces al día**

**Formato**:
- Completamente libre - bullets, frases sueltas, lo que sea
- Sin estructura obligatoria
- Fechas opcionales (solo si ayuda)

**Cleanup**:
- **Semanal**: Revisar y migrar notas importantes a learning-journal
- **Mensual**: **PURGAR TODO** al final del mes - empezar limpio

**Ejemplo real**:
```markdown
# Scratch Notes

> ⚡ Ultra-fast notes - no structure required

---
23/12/2025.
- 1 Scenario = 1 Use Case
- Si el Use case tiene ramificaciones se incluyen en la clase
  y se parametriza el test case.

24/12/2025
- Bug: NavigationScenario recibe URL hardcoded 🤔
- TODO: Ver pytest parametrize
- Link interesante: [...]

25/12/2025
✅ Arreglado bug de NavigationScenario
Idea: ¿BaseScenario con métodos comunes?
```

**Filosofía**: Escribe rápido, sin pensar. Migra lo bueno. Borra el resto.
---

### `workflows.md`
**Propósito**: Documentar ritmos y procesos de trabajo del proyecto.

**Contenido**:
- Rutina diaria/semanal
- Proceso de commits/PRs
- Cuándo escribir blog posts
- Cuándo preparar talks
- Checkpoints mensuales

**Actualización**:
- Según necesites ajustar tus procesos
- Review al final de cada mes

---

**Propósito**: Explicación de la arquitectura hexagonal del framework.

**Contenido**:
- Overview del patrón Ports & Adapters
- Estructura del framework
- Diagramas de componentes y flujo
- Guía de cómo agregar nuevos adapters/scenarios
- Links a ADRs relevantes

**Actualización**:
- Mes 1: Versión inicial
- Conforme evoluciona el framework

**Decisiones (ADRs)**: Ver [architecture/decisions/](architecture/decisions/README.md)

---

### `architecture/decisions/` (ADRs)
**Propósito**: Registro de decisiones arquitectónicas importantes.

**Cuándo crear un ADR**:
- Cambios significativos en estructura del framework
- Elección de herramientas principales
- Cambios que afectan múltiples meses del roadmap
- Cuando necesites linkear una decisión desde código

**Formato**:
- Usar `template.md` como base
- Numeración secuencial: `ADR-001-*.md`
- Tiempo: **30-60 min por ADR**

**Ejemplos actuales**:
- ADR-001: Arquitectura Hexagonal
- ADR-002: Selectores - Decisión de nombres
- ADR-003: Separación Common Locators

---

### `resources/useful-links.md`
**Propósito**: Centralizador de enlaces útiles, cheatsheets, referencias rápidas.

**Contenido**:
- Links a documentación oficial
- Tutoriales útiles
- Artículos de referencia
- Cheatsheets (Playwright, Pytest, etc.)

**Actualización**:
- Conforme encuentres recursos valiosos
- Organizado por tecnología/tema

---

## 📅 Documentación Mensual

Las retrospectivas y documentación específica de cada mes viven en:
```
months/
├── month-01-foundations/
│   ├── README.md           # Overview y entregables del mes
│   └── RETROSPECTIVE.md    # Reflexión al final del mes
├── month-02-architecture/
│   └── ...
└── README.md               # Índice de meses (roadmap visual)
```

Ver [months/README.md](../months/README.md) para navegación mensual.

---

## ⏱️ Tiempo Estimado por Documento

| Documento | Frecuencia | Tiempo | Prioridad | Notas |
|-----------|------------|--------|-----------|-------|
| **scratch.md** | Diario | 1-5 min | Alta | Sin estructura, escribe rápido |
| **learning-journal.md** | 2-3x/semana | ≤30 min | Alta | Solo si aprendiste algo valioso |
| **workflows.md** | Según necesidad | 15-30 min | Media | Ajustes a procesos |
| **architecture/README.md** | 1x/mes | 30-60 min | Media | Actualizar conforme evoluciona |
| **ADR** (nuevo) | Según decisión | 30-60 min | Variable | Solo decisiones importantes |
| **useful-links.md** | Ad-hoc | 5 min | Baja | Cuando encuentres algo útil |
| **Monthly RETROSPECTIVE.md** | 1x/mes | 2-3 hrs | Alta | Usa learning-journal + scratch como input |

---

## 🎯 Flujo de Trabajo Sugerido

### Durante el mes:
1. **scratch.md** → Notas rápidas mientras trabajo
2. **learning-journal.md** → Cuando estudio o tengo insights
3. **ADR** → Cuando tomo decisión arquitectónica importante
4. **useful-links.md** → Cuando encuentro recurso valioso

### Fin de mes:
1. **Revisar scratch.md** → Migrar lo importante a learning-journal
2. **Purgar scratch.md** → Empezar mes siguiente limpio
3. **Escribir RETROSPECTIVE.md** → En carpeta del mes correspondiente
4. **Actualizar workflows.md** → Si ajuste procesos

---

## 📚 Otros Recursos del Proyecto

- **[Roadmap completo](../months/README.md)** - Plan de 12 meses
- **[SUTs Setup](../suts/README.md)** - Cómo levantar cada sistema bajo prueba
- **[README principal](../README.md)** - Landing page del proyecto
- **[Learning Resources](../../learning-resources.md)** - Libros, cursos, tutoriales (archivo del proyecto Claude)

---

## 💡 Tips de Documentación

### Para learning-journal.md
- ✅ **Usa el template** - Es rápido una vez que te acostumbras
- ✅ **Main Takeaway primero** - Si solo tengo 5 min, escribiré esto
- ✅ **Tags consistentes** - Facilita buscar después (#playwright, #architecture, etc.)
- ✅ **Solo si vale la pena** - Está bien NO escribir algunos días
- ❌ **No documentar TODO** - Solo lo que quieres recordar en 3 meses

**Truco**: Si no puedo resumir en 1 frase (Main Takeaway), quizá no entendí bien el tema.

### Para scratch.md
- ✅ **Escribir SIN pensar** - Es mi bloc de notas mental
- ✅ **Fechas opcionales** - Solo si ayuda a recordar contexto
- ✅ **Copy-paste libre** - Comandos, errores, links temporales
- ✅ **Review semanal** - ¿Qué migro a learning-journal?
- ✅ **Purga mensual** - Borro TODO al final del mes, empieza limpio
- ❌ **No me preocupo por formato** - Esa es la idea

**Filosofía**: Scratch es desechable. Learning-journal es permanente.

### Para ADRs
- ✅ **Solo decisiones importantes** - Afectan estructura o múltiples meses
- ✅ **Linkea desde código** - `# Ver ADR-003` en comentarios
- ✅ **Contexto > Decisión** - Explica POR QUÉ, no solo QUÉ
- ❌ **No hacer ADR de todo** - 2-3 ADRs por mes es mucho

**Cuándo crear ADR**:
- Cambia arquitectura del framework
- Elijo herramienta principal (Playwright, Pact, k6, etc.)
- Decido estrategia que afecta futuros meses
- Cuando pienso "¿por qué decidí esto?" 3 meses después

### Para retrospectivas mensuales
- ✅ **Usar learning-journal como input** - Ya tengo el material
- ✅ **Usar scratch para recordar** - Problemas que encontré
- ✅ **Ser honesto** - Qué NO funcionó es tan valioso como qué sí
- ✅ **Métricas reales** - Tests escritos, commits, posts publicados
- ✅ **Ajustes concretos** - "En mes 2 haré X diferente porque Y"

**Template sugerido para retros** (crear en `months/month-XX/RETROSPECTIVE.md`):
```markdown
# Retrospectiva Mes XX

## ✅ Completado
- [Lista de entregables cumplidos]

## ⏳ Pendiente
- [Qué no se completó y por qué]

## 📚 Aprendizajes Clave
- [Top 3-5 cosas aprendidas]

## 🐛 Problemas Encontrados
- [Blockers, bugs, frustraciones]

## 💡 Insights
- [Cosas que cambiarían tu approach]

## 📊 Métricas
| Métrica | Target | Real | % |
|---------|--------|------|---|
| Tests   | 8      | 6    | 75% |

## 🔄 Ajustes para Próximo Mes
- [Cambios concretos al plan]
```
---

**Última actualización**: 3 Enero 2026
**Próxima revisión**: 31 Enero 2026 (fin de Mes 1)