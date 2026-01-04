# Workflows y Ritmos de Trabajo

Procesos y rutinas para mantener consistencia sin burnout durante el proyecto de aprendizaje 2026.

**Filosofía**: Progreso sostenible > Intensidad insostenible

**Última actualización**: 3 Enero 2026

---

## 🎯 Principios Guía

1. **Consistencia > Intensidad**: Mejor 1 hora diaria que 10 horas un día
2. **Flexibilidad > Rigidez**: La vida pasa - ajustar sin culpa
3. **Shipping > Perfección**: Código imperfecto en repo > código perfecto en tu cabeza
4. **Aprendizaje público**: Documentar proceso, no solo resultados
5. **Descanso intencional**: 1-2 días off por semana está bien

---

## 📅 Ritmo Semanal

### Distribución realista de tiempo

**Total semanal objetivo**: **8-12 horas** (no 15+)

**Días de semana (Lun-Vie)**: 1-2 hrs después del trabajo
**Fin de semana**: 2-4 hrs (sesión larga + review)
**Días off**: Mínimo 1 día completo sin trabajar en el proyecto

---

### 🔄 Estructura flexible por día

#### Lunes/Miércoles: Días de Estudio (opcional)

**Duración**: 1-2 hrs
**Objetivo**: Absorber conceptos, leer documentación
**Output**: Notas en `scratch.md`

**Actividades**:
- Leer docs oficiales (Playwright, Pytest, etc.)
- Ver tutoriales/videos
- Leer capítulos de libros del mes
- Experimentos pequeños (no código productivo)

**Formato libre** - puede ser:
- Lunes solo (2 hrs)
- Lunes + Miércoles (1 hr cada uno)
- Miércoles solo si lunes no pudiste
- **Skip si no tienes energía** (recuperar en fin de semana)

---

#### Martes/Jueves: Días de Código (opcional)

**Duración**: 1-2 hrs
**Objetivo**: Implementar pequeñas piezas, experimentar
**Output**: 1-3 commits

**Actividades**:
- Implementar scenario/adapter/test
- Refactorizar código existente
- Arreglar bugs
- Experimentos con herramientas

**Regla importante**: **No features grandes** - esas van al sábado

---

#### Viernes: Recovery Day

**Duración**: 0 hrs (día off)
**Objetivo**: Descansar, recuperar energía

**Permitido**:
- ✅ Leer algo ligero (artículo corto)
- ✅ Ver video de YouTube sobre el tema
- ✅ Pensar en el proyecto (sin laptop)

**No permitido**:
- ❌ Coding
- ❌ Escribir documentación
- ❌ "Solo voy a hacer esto rapidito" (trampa mental)

---

#### Sábado: Día de Flow

**Duración**: **2-4 hrs** (no 4-6 como antes)
**Objetivo**: Feature completa, avance significativo
**Output**: Feature funcionando + tests

**Estructura sugerida**:
```
09:00 - 09:15  Planning: ¿Qué voy a lograr hoy?
09:15 - 10:45  Coding session 1 (90 min)
10:45 - 11:00  Break
11:00 - 12:30  Coding session 2 (90 min)
12:30 - 13:00  Cleanup: commits, push, notas
```

**Alternativa flexible**:
- Si perdiste días durante la semana → 3-4 hrs
- Si ya avanzaste bien → 2 hrs suficiente
- Si hay evento (lightning talk, reunión DgoTecHub) → **Skip o reduce a 1 hr**

**Output típico**:
- 1 feature completa (scenario + tests)
- 5-10 commits
- Tests pasando

---

#### Domingo: Día de Review

**Duración**: 1-2 hrs
**Objetivo**: Reflexión, documentación, planning
**Output**: Journal entry, scratch migrado

**Estructura sugerida**:
```
17:00 - 17:30  Review de código de la semana
17:30 - 18:15  Migrar scratch.md → learning-journal.md
18:15 - 18:45  Planning semana siguiente (mental o escrito)
18:45 - 19:00  Cleanup: purgar scratch.md
```

**Template de weekly review**:
```markdown
## YYYY-MM-DD | Week XX Review

**⏱️ Tiempo esta semana**: ~X hrs
**🏷️ Tags**: #week-review

### 🏆 Logros
- Commits: X
- Tests escritos: X
- Aprendizajes clave: [1-2 bullets]

### 🚧 Obstáculos
- [Si hubo alguno]

### ➡️ Próxima semana
- Prioridad 1: [Feature/concepto principal]
- Prioridad 2: [Secundario]
```

**Alternativa mínima** (si no tienes 2 hrs):
- 30 min: Solo migrar scratch → journal
- Skip planning formal (hazlo mental)

---

## 📝 Sistema de Documentación

### Nivel 1: scratch.md (Captura Rápida)

**Propósito**: Notas ultra-rápidas durante el trabajo
**Tiempo**: 10-30 segundos por nota
**Estructura**: Ninguna (libre, bullets, lo que sea)
**Cleanup**: Semanal (domingos)

**Ejemplo**:
```markdown
# Scratch Notes

---
03/01/2026
- 1 Scenario = 1 Use Case
- Ramificaciones del UC → incluir en clase + parametrizar test
- Bug: NavigationScenario recibe URL 🤔

04/01/2026
✅ Arreglado bug NavigationScenario
Idea: ¿BaseScenario con métodos comunes?
```

**Filosofía**: Escribe sin pensar. Migra lo bueno. Borra el resto.

---

### Nivel 2: learning-journal.md (Aprendizaje Formal)

**Propósito**: Documentar aprendizajes con estructura
**Tiempo**: ≤30 min por entry
**Frecuencia**: 1-2x por semana (no diario)
**Permanencia**: Permanente

**Template** (ya lo tienes, es bueno):
```markdown
## YYYY-MM-DD | Título Descriptivo

**⏱️ Tiempo**: Xh | **📚 Fuente**: [recurso] | **🏷️ Tags**: #tag1 #tag2

### 💡 Main Takeaway
> "Una frase que resume lo más importante"

### 🔑 Conceptos clave
- Concepto 1
- Concepto 2

### 🎯 Aplicación inmediata
Cómo lo usarás en el proyecto

### ❓ Dudas pendientes
Preguntas que aún tienes

### ➡️ Next
Siguiente paso de aprendizaje
```

**Cuándo escribir**:
- Domingos (weekly review)
- Después de aprender algo importante
- **Solo si vale la pena** (no forzar entradas)

---

### Nivel 3: ADRs (Decisiones Arquitectónicas)

**Propósito**: Documentar decisiones importantes
**Tiempo**: 30-60 min por ADR
**Frecuencia**: 1-2x por mes (no más)

**Cuándo crear**:
- Cambio arquitectónico significativo
- Elección de herramienta principal
- Decisión que afecta múltiples meses
- Cuando necesites linkear desde código

**Usar tu template actual** (`docs/architecture/decisions/template.md`)

---

## 🗓️ Ritmo Mensual

### Semana 1: Setup + Exploración

**Objetivo**: Entender conceptos del mes, experimentar

**Actividades**:
- Leer sobre tema principal del mes
- Crear branch: `git checkout -b month-XX-topic`
- Experimentos y spikes
- Notas en scratch/journal

**Output**:
- Entendimiento conceptual
- Plan de implementación claro

---

### Semana 2: Implementación Core

**Objetivo**: Escribir código principal del framework

**Actividades**:
- Implementar ports/adapters/scenarios
- Escribir primeros tests (3-5)
- Commits frecuentes y pequeños
- Sábado = feature completa

**Output**:
- Framework evolucionado
- 3-5 tests funcionando
- Estructura básica completa

---

### Semana 3: Refinamiento

**Objetivo**: Completar tests, pulir código

**Actividades**:
- Agregar tests faltantes (total 6-8)
- Refactorizar código
- Documentar (README del mes)
- Preparar para merge

**Output**:
- 6-8 tests completos (75-100% del target)
- Código limpio
- Branch lista para merge

---

### Semana 4: Documentación + Cierre

**Objetivo**: Retrospectiva, blog, merge

**Actividades**:
- Escribir retrospectiva mensual
- Merge branch a main
- Tag del mes: `git tag month-XX-topic`
- Comenzar blog post (si aplica)
- Prep de talk (si es mes con presentación)

**Output**:
- Retrospectiva completa
- Branch mergeada
- Blog post draft (publicar en primeros días del siguiente mes)

---

## 🌿 Sistema de Branches

### Estrategia (desde Mes 1)
```
main
  ├── month-01-foundations
  ├── month-02-architecture
  ├── month-03-contracts
  └── ...
```

### Workflow del mes
```bash
# Inicio del mes (Semana 1)
git checkout main
git pull
git checkout -b month-01-foundations

# Durante el mes - commits pequeños frecuentes
git add .
git commit -m "feat: add BrowserPort interface"
git push origin month-01-foundations

# Más commits incrementales
git commit -m "feat: implement PlaywrightAdapter"
git commit -m "test: add home page navigation tests (3 tests)"
git commit -m "refactor: centralize common locators"

# Semana 3-4 - preparar cierre
git commit -m "docs: update month-01 README with progress"
git commit -m "docs: complete month-01 retrospective"

# Semana 4 - merge
git checkout main
git merge month-01-foundations
git tag month-01-foundations
git push origin main --tags

# Opcional: mantener branch como referencia histórica
# (no borrar - útil para ver evolución)
```

### Convenciones de commits

**Formato**: `<type>: <description>`

**Types**:
- `feat`: Nueva funcionalidad
- `test`: Agregar/modificar tests
- `refactor`: Cambio de código sin cambiar funcionalidad
- `docs`: Solo documentación
- `fix`: Corrección de bugs
- `chore`: Tareas de mantenimiento

**Ejemplos**:
```bash
feat: add NavigationScenario with go_to methods
test: add 3 tests for blog navigation
refactor: extract common locators to separate file
docs: update month-01 README
fix: resolve flaky test in home page
chore: update pytest to 8.3.4
```

**Regla**: Commits pequeños y frecuentes > commits gigantes

---

## ⚡ Manejo de Imprevistos

### Cuando pierdes días (enfermedad, trabajo, familia)

**1-2 días perdidos**:
- ✅ Recuperar en fin de semana (agregar 1 hr extra)
- ✅ Seguir con el plan normal

**3-4 días perdidos**:
- ✅ Sábado = recuperación (3-4 hrs en vez de 2-3)
- ✅ Reducir scope si es necesario (6 tests en vez de 8)

**1 semana completa perdida**:
- ✅ Reducir scope del mes (50%)
- ✅ Enfocarse en lo esencial: 1 feature + 3-4 tests + retrospectiva
- ✅ NO intentar "catch up" - solo te quemarás

**Filosofía**: **Mejor entregar menos bien hecho que abandonar el proyecto**

---

### Días con eventos especiales

**Lightning talk ese día**:
- ❌ No planees coding ese día
- ✅ Usa el día para preparación final de la talk
- ✅ Recupera horas otro día

**Reunión DgoTecHub**:
- ❌ No planees sesión larga
- ✅ Máximo 1 hr de código ligero
- ✅ Cuenta como "día de comunidad" (también es parte del proyecto)

**Compromiso familiar**:
- ✅ Skip sin culpa
- ✅ Recupera si puedes, si no, ajusta scope

---

## 📊 Métricas de Éxito

### Semanales (informal)

- ⏱️ **Tiempo**: 8-12 hrs
- 💻 **Commits**: 3-10
- ✅ **Tests**: 1-3 nuevos
- 📝 **Journal**: 1 entry (mínimo)

**No obsesionarse** - son guías, no mandatos

---

### Mensuales (tracking formal)

| Métrica | Target | Mínimo Aceptable |
|---------|--------|------------------|
| Tiempo invertido | 40-50 hrs | 30 hrs |
| Commits | 15-30 | 10 |
| Tests escritos | 8-10 | 6 |
| Journal entries | 4-6 | 2 |
| Blog posts | 1 | 1 (draft ok) |
| Retrospectiva | 1 | 1 |
| Talk (si aplica) | 1 | 1 |

**En retrospectiva mensual**: Trackear real vs target, ajustar expectations

---

## 🚨 Red Flags y Recuperación

### Señales de alerta

**🔴 Sin commits por 1 semana**:
- Hacer commit aunque sea de docs
- Identificar blocker

**🔴 Escribiste código que no entiendes**:
- STOP. Borrar. Reescribir manualmente
- Entender > velocidad

**🔴 Journal vacío por 2+ semanas**:
- Session de 30 min solo de journal
- ¿Perdiste el hábito de reflexión?

**🔴 Te sientes quemado**:
- **Recovery week**: Reducir a 50% del tiempo
- Solo lo esencial (1-2 hrs/semana)
- Está bien tomar break de 1 semana

---

### Recovery protocol (si vas MUY atrasado)
```markdown
## Recovery Plan

**STOP. Breathe. Evaluate.**

Prioridad 1 (Must have):
- [ ] 1 feature core implementada
- [ ] 3-4 tests funcionando
- [ ] Retrospectiva escrita (aunque sea breve)

Prioridad 2 (Nice to have):
- [ ] Tests extras (hasta 8)
- [ ] Refactors
- [ ] ADR formal

Skip temporal:
- ❌ Blog post detallado (draft rápido ok)
- ❌ Perfeccionismo en código
- ❌ Documentación exhaustiva

**Regla**: Mejor entregar 50% bien hecho que 0%
```

---

## 💡 Tips Anti-Burnout

### Energy Management

- ✅ Máximo 4 hrs de código en un día
- ✅ Breaks cada 90 min (Pomodoro o similar)
- ✅ 1-2 días completos off por semana
- ✅ Si estás cansado → skip o reduce tiempo (no forzar)

### Motivation Hacks

- 🎯 Reeler `my-commitments.md` cuando dudes
- 🏆 Celebrar wins pequeños (test pasando, commit, insight)
- 📊 Ver git graph crecer: `git log --graph --oneline`
- 👥 Compartir progreso públicamente (accountability)

### Flexibility

- ✅ Ajustar workflows según aprendes
- ✅ Revisar este documento cada mes
- ✅ Cambiar lo que no funciona **sin culpa**

**Filosofía**: Este documento te sirve a ti, no tú a este documento

---

## 🎓 Aprendizaje sin Atajos

### Reglas de Disciplina

1. **NO Copilot** durante el proyecto
   - Escribes cada línea manualmente
   - Entiendes lo que escribes

2. **NO Copy-Paste ciego**
   - De Claude, Stack Overflow, o tutoriales
   - Puedes inspirarte, pero reescribe en tus palabras

3. **Coding challenges semanales** (opcional pero recomendado)
   - 1x por semana, 30-60 min
   - Sin ayuda de AI
   - Valida que realmente aprendes

### Filosofía

> "Si no puedes explicarlo con tus palabras, no lo entiendes"
> "Tardar 2 horas entendiendo > 10 min copy-pasting"

---

## 📚 Quick Reference

### ¿Qué hacer hoy?

| Día | Actividad Principal | Duración | Flexible? |
|-----|---------------------|----------|-----------|
| Lun/Mié | Estudio | 1-2 hrs | ✅ Sí |
| Mar/Jue | Código ligero | 1-2 hrs | ✅ Sí |
| Vie | OFF | 0 hrs | ❌ Respetar |
| Sáb | Flow (código) | 2-4 hrs | ⚠️ Ajustar según necesidad |
| Dom | Review + Journal | 1-2 hrs | ⚠️ Mínimo 30 min |

### Archivos a revisar

| Cuándo | Archivo | Para qué |
|--------|---------|----------|
| Antes de sesión | `months/month-XX/README.md` | Ver qué checkboxes atacar |
| Durante sesión | `scratch.md` | Capturar ideas rápidas |
| Domingos | `learning-journal.md` | Migrar y reflexionar |
| Fin de mes | `RETROSPECTIVE.md` | Cerrar el mes |

### Comandos útiles
```bash
# Ver progreso semanal
git log --since="1 week ago" --oneline

# Contar commits del mes
git log --since="1 month ago" --oneline | wc -l

# Ver tests disponibles
pytest tests/ --collect-only

# Branch actual
git branch --show-current
```

---

## 🔄 Revisión de este Documento

- **Mensual**: En retrospectiva - ¿workflows funcionando?
- **Trim human (cada 3 meses)**: Review profundo - ¿ajustar algo?
- **Anual**: Gran review - ¿qué aprendiste sobre tu forma de trabajar?

**Regla de oro**: Si algo no te sirve, cámbialo. Este documento evoluciona contigo.

---

**Última actualización**: 3 Enero 2026
**Próxima revisión**: 31 Enero 2026 (fin de Mes 1)