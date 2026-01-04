# Roadmap 2026 - Documentación Mensual

Índice de los 12 meses del proyecto de aprendizaje, con acceso rápido a documentación, retrospectivas y progreso.

---

## 📅 Calendario Visual
```
2026

ENE ── Talk: "git init" (28 ene) ── Foundations + Blog E2E
FEB ── Taller: (TBD) ── Arquitectura + Microservicios
MAR ── Talk (opcional/video): "Arquitectura Hexagonal" ── Contract Testing
ABR ── (Sin evento) ── Observabilidad
MAY ── Talk (opcional/video): "Contract Testing" u "Observabilidad" ── Test Data
JUN ── (Sin evento) ── CI/CD Avanzado
JUL ── Talk (opcional/video): "CI/CD Optimizado" ── Performance ── CHECKPOINT
AGO ── (Sin evento) ── Chaos Engineering
SEP ── Talk (opcional/video): "Chaos Engineering" ── Security Testing
OCT ── (Sin evento) ── Accessibility Testing
NOV ── (Sin evento) ── Test Strategy
DIC ── Talk final: "12 Meses" ── Capstone
```

**Nota sobre talks**: Las charlas pueden presentarse en el evento mensual de DgoTecHub
(sujeto a disponibilidad de slots y temática del mes) o grabarse como video.
El objetivo es siempre generar el contenido para práctica y compartir en el blog.

---

## 🗓️ Meses del Proyecto

### ✅ Completados

_(Ninguno aún - primero se completará Mes 1 en enero)_

---

### 🚧 En Progreso

#### [Month 01: Foundations + Hexagonal Architecture](month-01-foundations/)

**Período**: Enero 2026
**Status**: 🚧 En progreso (iniciado 1 Ene 2026)

**Objetivo**: Construir base del framework con arquitectura hexagonal usando el blog como primer SUT

**Entregables**:
- Framework: Ports, Adapters, Scenarios
- Tests: 6-8 tests E2E del blog
- **Talk**: "git init 'Mi proyecto 2026'" - Analogía Git para crecimiento personal
  - Usar tu roadmap como ejemplo práctico
  - Call to action: crear repos de aprendizaje público
- Blog: "Roadmap 2026: Test Architecture"

**Progreso**: 1/8 tests (12.5%)

**Documentación**:
- [📄 README del mes](month-01-foundations/README.md)
- ⏳ RETROSPECTIVE.md (se escribirá al final del mes)

---

### ⏳ Pendientes

#### Month 02: Architecture Refinement + Microservices

**Período**: Febrero 2026
**Status**: ⏳ Pendiente

**Objetivo**: Refactorizar framework hacia arquitectura más robusta, agregar microservicios FastAPI

**Herramientas nuevas**: HTTPX, FastAPI, Testcontainers Python

**Entregables**:
- API Port + adapters
- 2 Microservicios (Users, Content)
- 8-10 tests API
- Blog: 2 posts (arquitectura hexagonal + feedback del taller)

**Documentación**:
- ⏳ README (se creará en febrero)
- ⏳ RETROSPECTIVE.md

---

#### Month 03: Contract Testing

**Período**: Marzo 2026
**Status**: ⏳ Pendiente

**Objetivo**: Implementar Consumer-Driven Contracts con Pact

**Herramientas nuevas**: Pact Python, Pact Broker, WireMock

**Entregables**:
- Consumer tests (Content → Users)
- Provider tests (Users)
- Pipeline con Pact Broker
- Talk (opcional): "Arquitectura Hexagonal" o video grabado
- Blog: "Contract Testing con Pact"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 04: Observability

**Período**: Abril 2026
**Status**: ⏳ Pendiente

**Objetivo**: Implementar observabilidad completa (traces, logs, metrics)

**Herramientas nuevas**: OpenTelemetry, Grafana, Tempo, Loki

**Entregables**:
- Stack Grafana + Tempo + Loki
- Tests instrumentados con OTel
- Dashboards de métricas
- Blog: "Observabilidad para Test Automation"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 05: Test Data Management

**Período**: Mayo 2026
**Status**: ⏳ Pendiente

**Objetivo**: Dominar gestión de datos de prueba con factories

**Herramientas nuevas**: Factory Boy, Faker, Saleor (nuevo SUT)

**Entregables**:
- Factories para entidades principales
- Saleor desplegado localmente
- Tests usando factories
- Talk: "Contract Testing" u "Observabilidad"
- Blog: "Test Data Management"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 06: CI/CD Avanzado

**Período**: Junio 2026
**Status**: ⏳ Pendiente

**Objetivo**: Optimizar pipelines con paralelización y quality gates

**Herramientas nuevas**: pytest-xdist, pytest-testmon, SonarQube

**Entregables**:
- Pipeline paralelo (4 shards)
- Pipeline PR: <10 min
- Quality gates con SonarQube
- Blog: "Optimización de CI/CD"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 07: Performance Testing + Checkpoint

**Período**: Julio 2026
**Status**: ⏳ Pendiente

**Objetivo**: Testing de performance con SLOs/SLIs + retrospectiva de medio año

**Herramientas nuevas**: k6, InfluxDB

**Entregables**:
- 5 scripts de k6 (baseline, load, stress, spike, soak)
- SLOs definidos
- Dashboard de k6
- Talk: "Optimización de CI/CD"
- Blog: 2 posts (performance + retrospectiva 6 meses)
- **CHECKPOINT**: Documento de retrospectiva de 6 meses

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md
- ⏳ checkpoint-6-months.md

---

#### Month 08: Chaos Engineering

**Período**: Agosto 2026
**Status**: ⏳ Pendiente

**Objetivo**: Validar resiliencia con Chaos Engineering

**Herramientas nuevas**: Chaos Toolkit, Toxiproxy

**Entregables**:
- 5+ experimentos de chaos
- Steady-state probes
- Runbook de chaos
- Blog: "Chaos Engineering para QA"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 09: Security Testing

**Período**: Septiembre 2026
**Status**: ⏳ Pendiente

**Objetivo**: Testing de seguridad automatizado (SAST/DAST)

**Herramientas nuevas**: OWASP ZAP, Bandit, Semgrep

**Entregables**:
- SAST (Bandit + Semgrep)
- DAST (ZAP scans)
- Pipeline de seguridad
- Talk: "Chaos Engineering para QA"
- Blog: "Security Testing Automatizado"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 10: Accessibility Testing

**Período**: Octubre 2026
**Status**: ⏳ Pendiente

**Objetivo**: Testing de accesibilidad siguiendo WCAG 2.1 AA

**Herramientas nuevas**: axe-core, Pa11y, Lighthouse CI

**Entregables**:
- axe integrado en Playwright
- Pa11y en CI
- Lighthouse CI con budgets
- Blog: "Accessibility Testing Automatizado"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 11: Test Strategy + DORA Metrics

**Período**: Noviembre 2026
**Status**: ⏳ Pendiente

**Objetivo**: Desarrollar pensamiento estratégico con documento de test strategy

**Herramientas nuevas**: Metabase/Grafana para dashboards

**Entregables**:
- Documento de test strategy (25-30 páginas)
- 4 métricas DORA calculadas
- Dashboard de métricas
- Presentación ejecutiva
- Blog: "Métricas DORA para Test Engineering"

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md

---

#### Month 12: Capstone Project

**Período**: Diciembre 2026
**Status**: ⏳ Pendiente

**Objetivo**: Integrar todo el aprendizaje del año en proyecto capstone pulido

**Entregables**:
- Repositorio capstone completo
- 12 retrospectivas mensuales
- Video walkthrough (15-20 min)
- Diagramas C4 completos
- Todos los ADRs documentados
- Talk final: "12 Meses Aprendiendo Test Architecture"
- Blog: 2 posts (tour del repo + retrospectiva final)

**Documentación**:
- ⏳ README
- ⏳ RETROSPECTIVE.md
- ⏳ retrospectiva-anual.md

---

## 📊 Progreso General

**Última actualización**: 3 Enero 2026

| Mes | Tema | Tests | Talk/Video | Blog | Status |
|-----|------|-------|------|------|--------|
| 01 | Foundations | 1/8 | 28 Ene (DgoTecHub) | ⏳ | 🚧 |
| 02 | Architecture | 0/10 | ⏳ | ⏳ | ⏳ |
| 03 | Contracts | 0/8 | Video (no slot) | ⏳ | ⏳ |
| 04 | Observability | 0/8 | - | ⏳ | ⏳ |
| 05 | Test Data | 0/10 | ⏳ | ⏳ | ⏳ |
| 06 | CI/CD | 0/10 | - | ⏳ | ⏳ |
| 07 | Performance | 0/5 | ⏳ | ⏳ | ⏳ |
| 08 | Chaos | 0/6 | - | ⏳ | ⏳ |
| 09 | Security | 0/8 | ⏳ | ⏳ | ⏳ |
| 10 | Accessibility | 0/8 | - | ⏳ | ⏳ |
| 11 | Strategy | 0/5 | - | ⏳ | ⏳ |
| 12 | Capstone | - | ⏳ | ⏳ | ⏳ |

**Total anual**:
- Tests target: ~90
- Talks: 7
- Blog posts: 15

---

## 📝 Template de Retrospectiva

Cada mes incluye un archivo `RETROSPECTIVE.md` con esta estructura:
```markdown
# Month XX: [Nombre] - Retrospectiva

**Período**: [Mes] 2026
**Fecha de cierre**: DD Mes 2026

---

## 🎯 Objetivo del Mes

[Qué querías lograr según el roadmap]

---

## ✅ Completado

### Técnico
- [x] Entregable 1
- [x] Entregable 2
- [ ] Entregable 3 (pendiente)

### Contenido
- [x] Blog post publicado
- [x] Talk presentada (si aplica)

---

## ⏳ Pendiente

- [ ] Item que no se completó
- [ ] Razón por la que quedó pendiente

---

## 📚 Aprendizajes Clave

1. **Aprendizaje 1**: Descripción
2. **Aprendizaje 2**: Descripción
3. **Aprendizaje 3**: Descripción

---

## 🐛 Problemas Encontrados

- **Problema 1**: Descripción y cómo se resolvió (o no)
- **Problema 2**: Descripción

---

## 💡 Insights

- Insight 1 que cambió tu enfoque
- Insight 2 sobre el proceso

---

## 📊 Métricas

| Métrica | Target | Real | % |
|---------|--------|------|---|
| Tests escritos | 8 | 6 | 75% |
| Tiempo invertido | 40 hrs | 35 hrs | 87.5% |
| Commits | 20 | 18 | 90% |
| Blog posts | 1 | 1 | 100% |
| Talk (si aplica) | 1 | 1 | 100% |

---

## 🔄 Ajustes para Próximo Mes

### Qué mantener
- Lo que funcionó bien

### Qué cambiar
- Ajustes necesarios

### Qué dejar
- Lo que no aportó valor

---

## 🎯 Focus para Mes [X+1]

**Prioridades**:
1. Prioridad 1
2. Prioridad 2
3. Prioridad 3

**Preparación necesaria**:
- Setup/estudio previo para el siguiente mes

---

**Escrito**: DD Mes 2026
**Tiempo de escritura**: X hrs
```

---

## 🔗 Recursos Relacionados

- [Roadmap completo](../README.md) - Landing page del proyecto
- [Workflows](../docs/workflows.md) - Ritmos y procesos de trabajo
- [Learning Journal](../docs/learning-journal.md) - Aprendizajes continuos
- [Architecture Decisions](../docs/architecture/decisions/) - ADRs del proyecto

---

## 📅 Checkpoints Especiales

### Checkpoint Mes 7 (Medio Año)
Retrospectiva profunda de 6 meses:
- Métricas técnicas acumuladas
- Contenido generado (posts, talks)
- Engagement (blog visits, GitHub stars)
- Feedback del pitch (febrero)
- Aprendizajes clave
- Ajustes al plan para meses 7-12

### Checkpoint Mes 12 (Cierre Anual)
Retrospectiva completa del año:
- Todos los objetivos vs reales
- Repositorio capstone
- Video walkthrough
- Talk final
- Publicación del proyecto

---

**Última actualización**: 3 Enero 2026
**Próxima actualización**: 31 Enero 2026 (después de completar Mes 1)