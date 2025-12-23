# Workflows & Rhythms - Test Architecture Roadmap 2025

> Ritmos y procesos para mantener consistencia y calidad durante los 12 meses.

---

## 📅 Weekly Rhythm (Semana Típica)

### Distribución de Tiempo Base

**Total semanal**: 12-15 horas

| Día | Actividad Principal | Tiempo | Output | Notas |
|-----|---------------------|--------|--------|-------|
| **Lunes** | Estudio/Lectura | 2-3h | Entry en journal | Leer docs, artículos, conceptos |
| **Martes** | Código ligero | 1-2h | Commits pequeños | Experimentos, spikes, refactors |
| **Miércoles** | Estudio/Lectura | 2-3h | Entry en journal | Continuar aprendizaje conceptual |
| **Jueves** | Código ligero | 1-2h | Commits pequeños | Implementar lo aprendido |
| **Viernes** | Flexible | 0-2h | Variable | Recovery day si necesitas |
| **Sábado** | Código intensivo | 4-6h | Features completas | Chunk largo, flow state |
| **Domingo** | Review + Docs | 1-2h | Weekly review | Journal, planning, cleanup |

---

### Desglose por Actividad

#### Lunes & Miércoles: Días de Estudio
**Objetivo**: Absorber conceptos, leer documentación

**Estructura sugerida** (2-3 hrs):
```
19:00 - 19:15  Setup mental (café, ambiente)
19:15 - 20:30  Lectura enfocada (docs, artículos, libro)
20:30 - 20:40  Break
20:40 - 21:30  Práctica hands-on (ejemplos pequeños)
21:30 - 21:45  Notas en scratch.md
```

**Output**:
- Notas rápidas en `docs/scratch.md`
- Código de práctica en `practice/` (si aplica)

**NO hacer**:
- ❌ Implementar features del framework
- ❌ Escribir tests productivos
- ❌ Multitasking (solo estudio)

---

#### Martes & Jueves: Días de Código Ligero
**Objetivo**: Experimentar, implementar pequeñas piezas

**Estructura sugerida** (1-2 hrs):
```
19:00 - 19:10  Review de lo aprendido ayer
19:10 - 20:30  Coding (pequeños commits)
20:30 - 20:45  Notas rápidas en scratch.md
```

**Output**:
- 1-3 commits pequeños
- Spikes, experimentos, refactors menores

**Ejemplos**:
- Agregar un método nuevo a un port
- Refactorizar un locator
- Experimentar con una fixture nueva

**NO hacer**:
- ❌ Features grandes (dejar para sábado)
- ❌ Cambios arquitectónicos (necesitan más tiempo)

---

#### Sábado: Día de Flow (Código Intensivo)
**Objetivo**: Implementar features completas, avanzar significativamente

**Estructura sugerida** (4-6 hrs):
```
09:00 - 09:15  Planning: ¿Qué voy a lograr hoy?
09:15 - 11:00  Coding session 1
11:00 - 11:15  Break (caminar, café)
11:15 - 13:00  Coding session 2
13:00 - 14:00  Lunch break
14:00 - 15:30  Coding session 3 (o Testing/Refactor)
15:30 - 16:00  Cleanup: commits, push, notas rápidas
```

**Output**:
- Feature completa implementada
- 5-10 commits
- Tests pasando
- Branch lista para merge (o mergeada)

**Tips**:
- Apagar notificaciones
- Música sin letra o silencio
- Tener agua/snacks a la mano
- NO revisar redes sociales

**NO hacer durante estas horas**:
- ❌ Leer artículos nuevos (distraen del flow)
- ❌ Saltar entre features (enfócate en 1)
- ❌ Perfeccionismo (progreso > perfección)

---

#### Domingo: Día de Reflexión
**Objetivo**: Revisar semana, documentar aprendizajes, planear siguiente semana

**Estructura sugerida** (1-2 hrs):
```
17:00 - 17:30  Review del código de la semana
17:30 - 18:15  Migrar scratch.md → learning-journal.md
18:15 - 18:45  Planning semana siguiente
18:45 - 19:00  Cleanup: borrar scratch migrado
```

**Output**:
- Entry semanal en `learning-journal.md`
- `scratch.md` limpio (migrado lo importante)
- Plan de la próxima semana (mental o escrito)

**Template de review**:
```markdown
## YYYY-MM-DD | Week XX Review

**Tiempo invertido**: Xh | **Tags**: #week-review

### 🏆 Logros de la semana
- Commits: X
- Tests escritos: X
- Features completadas: X

### 💡 Aprendizajes clave
- Concepto 1
- Concepto 2

### 🚧 Obstáculos encontrados
- Problema X → Solución Y

### 🎯 Disciplina check
- ¿Escribí código sin entenderlo? SÍ/NO
- ¿Usé Copilot? NO ✅
- ¿Hice coding challenge sin ayuda? SÍ/NO

### ➡️ Próxima semana
- Prioridad 1
- Prioridad 2

---
```

---

## 📝 Sistema de 3 Niveles de Notas

### Nivel 1: scratch.md (Captura Rápida)

**Propósito**: Notas ultra-rápidas durante el trabajo
**Tiempo**: 10-30 segundos por nota
**Estructura**: Ninguna (raw, bullets, lo que sea)
**Permanencia**: Temporal (se migra o borra semanalmente)

**Cuándo usar**:
- Durante coding: encontraste algo interesante
- Durante lectura: aha moment
- Durante debugging: solución a un bug
- Cualquier pensamiento que quieras capturar SIN romper flow

**Ejemplo**:
```markdown
## 2024-12-22 14:30
Playwright tiene .first y .last para múltiples matches.
Para elemento único usar directamente locator().

## 2024-12-23 10:15
Bug: HomePageLocators.BLOG_TITLE no funciona si el componente
no tiene data-testid. Verificar SIEMPRE en el HTML.
```

**NO escribir**:
- ❌ Análisis profundos (dejar para journal)
- ❌ Formato fancy (es temporal)
- ❌ Código completo (usar comments en el código mismo)

---

### Nivel 2: learning-journal.md (Aprendizaje Formal)

**Propósito**: Documentar aprendizajes con estructura
**Tiempo**: 10-30 minutos por entry
**Estructura**: Template definido
**Permanencia**: Permanente (no se borra nunca)

**Cuándo usar**:
- Domingos (weekly review)
- Después de aprender algo importante
- Cuando terminas un módulo/concepto

**Template**:
```markdown
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
```

**Fuentes comunes**:
- Migración desde `scratch.md`
- Reflexión después de coding session
- Lectura de artículos/docs
- Debugging de problemas complejos

---

### Nivel 3: architecture/decisions.md (ADRs)

**Propósito**: Documentar decisiones arquitectónicas importantes
**Tiempo**: 1-2 horas por ADR
**Estructura**: Formato ADR (Architecture Decision Record)
**Permanencia**: Permanente, alta calidad

**Cuándo usar**:
- Decisión arquitectónica significativa
- Trade-offs importantes
- Cambios que afectan estructura del proyecto

**Template**:
```markdown
## ADR-XXX: Título de la Decisión

**Fecha**: YYYY-MM-DD
**Status**: 🤔 Proposed | ✅ Accepted | ❌ Rejected | ⚠️ Deprecated

### Contexto
¿Qué problema estamos resolviendo?

### Decisión
¿Qué decidimos hacer?

### Consecuencias

**Positivas**:
- ✅ Pro 1
- ✅ Pro 2

**Negativas**:
- ⚠️ Con 1
- ⚠️ Con 2

### Alternativas Consideradas
- Opción A: Por qué se rechazó
- Opción B: Por qué se rechazó

### Referencias
- Link 1
- Link 2

---
```

**Ejemplos de decisiones que merecen ADR**:
- Usar arquitectura hexagonal
- Organizar tests por SUT vs por tipo
- Estrategia de branching (mes por branch)
- Desactivar Copilot durante aprendizaje

---

### Flujo Entre Niveles
```
Durante el día/semana:
    ↓
scratch.md (notas rápidas)
    ↓ (migrar domingos)
learning-journal.md (entradas formales)
    ↓ (cuando hay decisión arquitectónica)
architecture/decisions.md (ADRs)
```

**Ejemplo de flujo**:
```
Lunes: Leo sobre hexagonal architecture
  → scratch.md: "Ports son interfaces, adapters son implementaciones"

Miércoles: Implemento BrowserPort
  → scratch.md: "ABC en Python = abstract class"

Sábado: Implemento framework completo
  → scratch.md: "Separar locators de adapters funciona bien"

Domingo: Weekly review
  → learning-journal.md: Entry completo sobre hexagonal
  → Migro ideas de scratch.md
  → Borro lo migrado de scratch.md

Lunes siguiente: Decido usar hexagonal para todo el año
  → architecture/decisions.md: ADR-001 sobre hexagonal
```

---

## 🗓️ Monthly Rhythm (Ritmo Mensual)

### Semana 1: Setup + Aprendizaje Base
**Enfoque**: Estudiar conceptos del mes, experimentar

**Actividades**:
- Leer sobre el tema principal del mes
- Crear branch del mes: `git checkout -b month-XX/topic`
- Implementar spikes/experimentos
- Notas en scratch.md → journal dominical

**Output esperado**:
- Conocimiento conceptual sólido
- Experimentos en `practice/` o similar
- Plan de implementación

---

### Semana 2: Implementación Core
**Enfoque**: Escribir el código principal del mes

**Actividades**:
- Implementar ports/adapters/scenarios nuevos
- Escribir primeros tests
- Commits frecuentes, pequeños
- Sábado = feature grande

**Output esperado**:
- Framework evolucionado
- 3-5 tests nuevos
- Código funcionando básico

---

### Semana 3: Refinamiento + Merge
**Enfoque**: Pulir, testear, preparar para producción

**Actividades**:
- Agregar tests faltantes
- Refactorizar código
- Documentar (README del mes)
- Merge a main

**Output esperado**:
- 8-10 tests completos
- Código limpio, con docstrings
- Branch mergeada a main
- Tag del mes: `git tag -a v1.0-month-01`

---

### Semana 4: Documentación + Publicación
**Enfoque**: Blog post, retro, talk prep (si aplica)

**Actividades**:
- Escribir blog post draft
- Completar retrospectiva mensual
- Preparar talk (meses con presentación)
- Publicar blog post
- Anunciar en redes

**Output esperado**:
- Blog post publicado
- Retrospectiva en `months/month-XX/`
- Talk lista (si aplica)
- Proyecto anunciado públicamente

---

## 🔄 Workflow de Git (Branching)

### Branch Strategy
```
main
  ├── month-01/foundations    (ene)
  ├── month-02/architecture   (feb)
  ├── month-03/contracts      (mar)
  └── ...
```

### Durante el Mes
```bash
# Inicio del mes
git checkout main
git pull
git checkout -b month-01/foundations

# Durante el mes - commits pequeños y frecuentes
git add .
git commit -m "feat: add BrowserPort interface"
git push origin month-01/foundations

# Commits incrementales
git commit -m "feat: add PlaywrightAdapter"
git commit -m "test: add home page tests (3 tests)"
git commit -m "refactor: centralize locators"

# Semana 3 - preparar merge
git commit -m "docs: add month-01 README"
git commit -m "retro: complete month-01 retrospective"

# Merge a main
git checkout main
git merge month-01/foundations
git tag -a v1.0-month-01 -m "Month 01: Foundations complete"
git push origin main --tags

# Opcional: borrar branch (o mantener como referencia)
# git branch -d month-01/foundations
```

### Commit Conventions
```bash
# Features
feat: add [component]
feat(framework): add BrowserPort interface
feat(tests): add blog E2E suite

# Tests
test: add [suite]
test(e2e): add home page tests
test(api): add users CRUD tests

# Refactor
refactor: improve [component]
refactor(adapter): simplify error handling

# Docs
docs: update [document]
docs(monthly): add month-01 README
docs(retro): complete retrospective

# Chore
chore: update dependencies
chore(ci): optimize pipeline

# Fix
fix: resolve [issue]
fix(tests): flaky test in blog navigation
```

---

## 🎯 Accountability Checkpoints

### Daily (Opcional)
- Quick note en `scratch.md` si hay insight
- Commit si hubo código

### Weekly (Obligatorio - Domingos)
```markdown
## Checklist Semanal

- [ ] Tiempo invertido esta semana: ___ horas
- [ ] Commits realizados: ___
- [ ] Tests escritos: ___
- [ ] scratch.md migrado a journal: ✅
- [ ] Planning próxima semana: ✅

### Disciplina Check
- [ ] ¿Usé Copilot? NO ✅
- [ ] ¿Escribí código sin entenderlo? NO ✅
- [ ] ¿Hice coding challenge? SÍ/NO
```

### Monthly (Obligatorio - Última Semana)
```markdown
## Checklist Mensual

### Código
- [ ] Framework evolucionado (ports/adapters/scenarios)
- [ ] Tests nuevos: ___ (target: 8-10)
- [ ] Tests viejos siguen pasando: ✅
- [ ] README del mes actualizado
- [ ] Branch mergeada a main
- [ ] Tag creado: vX.0-month-XX

### Documentación
- [ ] Learning journal actualizado
- [ ] Retrospectiva mensual completa
- [ ] Blog post draft terminado
- [ ] Blog post publicado

### Presentaciones (si aplica)
- [ ] Lightning talk preparada
- [ ] Talk presentada
- [ ] Video obtenido

### Publicación
- [ ] Proyecto anunciado (Twitter/LinkedIn)
- [ ] Repo actualizado en GitHub
```

---

## 🚨 Red Flags & Recovery

### Señales de Alerta

**🔴 Red Flag 1**: Más de 3 días sin commits
- **Acción**: Hacer commit pequeño (aunque sea docs)
- **Root cause**: ¿Bloqueado? ¿Falta de tiempo? ¿Perfeccionismo?

**🔴 Red Flag 2**: Escribiste código que no entiendes
- **Acción**: STOP. Borrar y reescribir manualmente
- **Root cause**: ¿Usaste Copilot? ¿Copy-paste de Claude?

**🔴 Red Flag 3**: Semana completa sin estudiar
- **Acción**: Mini-session de 1 hora en fin de semana
- **Root cause**: ¿Trabajo pesado? ¿Burnout?

**🔴 Red Flag 4**: Journal vacío por 2+ semanas
- **Acción**: Write now session de 30 min
- **Root cause**: ¿Perdiste el hábito? ¿Falta de reflexión?

---

### Recovery Protocols

**Si te atrasas 1 semana**:
```markdown
## Recovery Plan - 1 Week Behind

Prioridad 1 (Must have):
- [ ] 1 feature core implementada
- [ ] 3 tests mínimos
- [ ] 1 entry en journal

Prioridad 2 (Nice to have):
- [ ] Refactors
- [ ] Tests extras
- [ ] Docs extensas

Skip si es necesario:
- ❌ Blog post (publicar parcial o posponer)
- ❌ Coding challenges extras
- ❌ Perfeccionismo en código
```

**Si te atrasas 2+ semanas**:
```markdown
## Recovery Plan - 2+ Weeks Behind

STOP. Breath. Evaluate.

1. ¿Es problema de tiempo? → Ajustar expectativas del mes
2. ¿Es problema de energía? → Recovery week (reduce scope)
3. ¿Es problema de interés? → Re-evaluar roadmap

Acción:
- Reduce scope del mes actual (50% menos tests)
- Mantén lo esencial: 1 feature + 3 tests + 1 retro
- No intentes "catch up" el mes siguiente (burnout)
- Ajusta plan going forward
```

---

## 💪 Mantener Momentum

### Técnicas Anti-Burnout

**🔋 Energy Management**:
- No coder más de 6 horas en un día
- Breaks cada 90 min
- Un día completo off por semana (viernes o domingo)

**🎯 Motivation Hacks**:
- Visualizar: "En diciembre 2025, soy Test Architect"
- Reread `my-commitments.md` cuando dudes
- Celebrar wins pequeños (commit, test pasando, insight)

**👥 Social Accountability**:
- Anunciar progreso en redes (mensual)
- Compartir blog posts públicamente
- Accountability partner (check-ins mensuales)

**📊 Track Progress**:
- Git graph visual: `git log --graph --oneline`
- Ver crecer el número de tests
- Reler retrospectivas pasadas

---

## 🎓 Learning Philosophy

### Principios Guía

1. **Progreso > Perfección**
   - 1 test imperfecto > 0 tests perfectos
   - Iterar, no esperar el código perfecto

2. **Entendimiento > Velocidad**
   - Mejor tardar 2 horas entendiendo que 10 min copy-pasting
   - Si no puedes explicarlo, no lo entiendes

3. **Consistencia > Intensidad**
   - 2 horas/día durante 7 días > 14 horas en 1 día
   - El aprendizaje necesita tiempo de procesamiento

4. **Público > Privado**
   - Aprender en público genera accountability
   - Compartir = solidificar conocimiento
   - Feedback de comunidad = crecimiento acelerado

5. **Disciplina > Motivación**
   - La motivación es temporal
   - La disciplina es un sistema
   - Los hábitos > emociones del día

---

## 📚 Quick Reference

### Files to Check

| Cuándo | Archivo | Por Qué |
|--------|---------|---------|
| Inicias sesión | `my-commitments.md` | Recordar reglas |
| Durante coding | `scratch.md` | Capturar ideas |
| Domingos | `learning-journal.md` | Migrar y reflexionar |
| Fin de mes | `months/month-XX/retro.md` | Retrospectiva |
| Duda arquitectónica | `architecture/decisions.md` | Ver decisiones pasadas |

### Commands to Run
```bash
# Ver progreso semanal
git log --since="1 week ago" --oneline

# Contar commits del mes
git log --since="1 month ago" --oneline | wc -l

# Ver tests
pytest tests/ --collect-only

# Status general
git status
```

---

## 🎯 Success Metrics

### Weekly
- ⏱️ Tiempo invertido: 12-15 hrs
- 💻 Commits: 5-10
- ✅ Tests escritos: 1-3
- 📝 Journal entries: 1 (mínimo)

### Monthly
- ⏱️ Tiempo invertido: 50-60 hrs
- 💻 Commits: 20-30
- ✅ Tests escritos: 8-10
- 📝 Journal entries: 4-6
- 📄 Blog posts: 1
- 🎤 Talks: 0-1 (según mes)

### Annual (Goal)
- ⏱️ Tiempo invertido: ~600 hrs
- 💻 Commits: 250-350
- ✅ Tests escritos: 80-100
- 📝 Journal entries: 50-60
- 📄 Blog posts: 15
- 🎤 Talks: 7

---

**Última actualización**: 22 Diciembre 2024
**Revisión**: Ajustar según retrospectivas mensuales