# Test Architecture Learning - Roadmap 2026

🚀 Mi proyecto de aprendizaje: 12 meses aprendiendo sobre Test Architecture

---

## 🎯 Objetivo

Dominar test architecture a través de un roadmap estructurado que cubre:

| Mes | Tema | Talk | Blog | Tests | Status |
|-----|------|------|------|-------|--------|
| 01 | Foundations + Hexagonal | 28 Ene | ⏳ | 5/10 | 🚧 |
| 02 | Architecture + Microservices | Feb | ⏳ | 0/10 | ⏳ |
| 03 | Contract Testing | Mar | ⏳ | 0/8 | ⏳ |
| 04 | Observability | - | ⏳ | 0/8 | ⏳ |
| 05 | Test Data Management | May | ⏳ | 0/10 | ⏳ |
| 06 | CI/CD Avanzado | - | ⏳ | 0/10 | ⏳ |
| 07 | Performance Testing | Jul | ⏳ | 0/5 | ⏳ |
| 08 | Chaos Engineering | - | ⏳ | 0/6 | ⏳ |
| 09 | Security Testing | Sep | ⏳ | 0/8 | ⏳ |
| 10 | Accessibility Testing | - | ⏳ | 0/8 | ⏳ |
| 11 | Test Strategy + DORA | - | ⏳ | 0/5 | ⏳ |
| 12 | Capstone Project | Dic | ⏳ | - | ⏳ |

---

## 📁 Estructura del Proyecto
```
.
├── framework/       # Framework de testing (evoluciona mensualmente)
├── tests/           # Tests organizados por tipo y SUT
├── suts/            # Documentación de sistemas bajo prueba
├── docs/            # Documentación general y arquitectura
├── months/          # Documentación y retrospectivas mensuales
└── .github/         # CI/CD pipelines (desde mes 2)
```

---

## 🧪 Systems Under Test (SUTs)

Este framework prueba múltiples aplicaciones a lo largo del año:

| SUT | Meses | Stack | Repo |
|-----|-------|-------|------|
| **Blog Personal** | 1-3 | Astro + Keystatic | [ignaciops/ignaciopsdev-blog](https://github.com/ignaciops/ignaciopsdev-blog) |
| **Microservicios** | 2-6 | FastAPI + PostgreSQL | `microservices/` (este repo) |
| **Saleor** | 5-12 | Django + GraphQL | [saleor/saleor](https://github.com/saleor/saleor) |
| **Juice Shop** | 9 | Node.js + Angular | [juice-shop](https://github.com/juice-shop/juice-shop) |

📖 Ver [suts/README.md](suts/README.md) para instrucciones de setup detalladas.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.14+
- Docker & Docker Compose
- Node.js 20+ (para algunos SUTs)
- Git

### Setup del Framework
```bash
# 1. Clonar repo
git clone https://github.com/ignaciops/test-architecture-learning.git
cd test-architecture-learning

# 2. Setup Python environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -e .
playwright install --with-deps

# 4. Verify setup
pytest tests/ --collect-only
```

### Setup de SUTs (ejemplo Mes 1: Blog)
```bash
# En directorio paralelo (fuera de test-architecture-learning/)
cd ..
git clone https://github.com/ignaciops/ignaciopsdev-blog.git
cd ignaciopsdev-blog

# Install y run
npm install
npm run dev  # Corre en http://localhost:4321
```

### Run Tests
```bash
# Asegúrate que el blog esté accesible (prod o local)

# Run all tests
pytest tests/ -v

# Run with browser visible
pytest tests/ --headed -v

# Generate Allure report
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

> 📝 **Nota sobre estructura**: En Mes 1 todos los tests están en `tests/`.
> Desde Mes 2 se organizarán en `tests/e2e/` y `tests/api/` conforme el
> framework crece.
```

---

## ⚙️ Configuración de Ambientes

### Blog Personal (Mes 1-3)

Por default, los tests del blog corren contra **producción** (`https://ignaciops.dev`).

**¿Por qué?** El blog es estático y read-only - no hay riesgo de side effects.
```bash
# Default: contra producción (no requiere setup)
pytest tests/e2e/blog/ -v

# Override: contra local (si estás desarrollando)
BLOG_BASE_URL=http://localhost:4321 pytest tests/e2e/blog/ -v
```

**Para correr contra local**:
```bash
# Terminal 1: Levantar blog
cd ../blog
npm run dev  # Corre en http://localhost:4321

# Terminal 2: Tests contra local
cd test-architecture-learning
BLOG_BASE_URL=http://localhost:4321 pytest tests/e2e/blog/ -v
```

### Otros SUTs (Mes 2+)

Los demás sistemas (microservicios, Saleor, Juice Shop) **siempre corren contra ambientes locales** por seguridad.

Ver [suts/README.md](suts/README.md) para setup específico de cada uno.

---

## 📚 Documentación

- **[Índice de Docs](docs/README.md)** - Navegación de toda la documentación
- **[Learning Journal](docs/learning-journal.md)** - Aprendizajes diarios/semanales
- **[Workflows](docs/workflows.md)** - Ritmos y procesos de trabajo
- **[Arquitectura](docs/architecture/README.md)** - Overview del framework hexagonal
- **[ADRs](docs/architecture/decisions/)** - Architecture Decision Records
- **[Roadmap Mensual](months/README.md)** - Retrospectivas y progreso por mes

---

## 🧪 Tech Stack

### Core
- **Language**: Python 3.14+
- **E2E Testing**: Playwright
- **API Testing**: HTTPX (desde mes 2)
- **Test Framework**: Pytest
- **Reporting**: Allure
- **Architecture**: Hexagonal (Ports & Adapters)

### Infrastructure
- **Containers**: Docker + docker-compose
- **CI/CD**: GitHub Actions (desde mes 2)
- **VCS**: Git + GitHub

### Herramientas por Mes
- **Mes 3**: Pact (contract testing)
- **Mes 4**: OpenTelemetry, Grafana, Tempo, Loki
- **Mes 5**: Factory Boy, Faker, Saleor GraphQL
- **Mes 6**: pytest-xdist, SonarQube
- **Mes 7**: k6 (performance), InfluxDB
- **Mes 8**: Chaos Toolkit, Toxiproxy
- **Mes 9**: OWASP ZAP, Bandit, Semgrep
- **Mes 10**: axe-core, Pa11y, Lighthouse CI
- **Mes 11**: DORA metrics, Metabase

---

## 📊 Métricas Actuales

**Última actualización**: 3 Enero 2026

| Métrica | Actual | Target | Status |
|---------|--------|--------|--------|
| Tests E2E | 5 | 10 (mes 1) | 🚧 50% |
| Tests API | 0 | 10 (mes 2) | ⏳ |
| Pipeline Time | N/A | <10 min | ⏳ |
| Blog Posts | 0 | 15 (año) | ⏳ 0% |
| Lightning Talks | 0 | 7 (año) | ⏳ 0% |
| Total Commits | TBD | - | - |
| GitHub Stars | TBD | - | - |

---

## 🗂️ Progreso Detallado

Ver [months/README.md](months/README.md) para roadmap visual completo y retrospectivas mensuales.

---

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal, pero:

- ⭐ **Stars** son bienvenidas (¡motivación++!)
- 💬 **Feedback** en [Discussions](../../discussions)
- 🐛 **Issues** si encuentras algo roto
- 📖 **Ideas** para futuros meses

**No aceptando PRs** (es aprendizaje personal), pero todo feedback es apreciado.

---

## 📞 Sígueme

- 📝 **Blog**: [ignaciops.dev](https://ignaciops.dev)
- 💼 **LinkedIn**: [Ignacio PS](https://linkedin.com/in/ignaciops)
- 🐦 **Twitter/X**: [@ignaciopsdev](https://x.com/ignaciopsdev)
- 🎥 **Talks**: [Playlist YouTube](#) ← (Próximamente)

¿Eres de Durango, MX? Te invito a unirte al [servidor de Discord de DgoTecHub](https://discord.gg/JgU4m4aqE5)!!
---

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE)

---

## 🙏 Agradecimientos

- Comunidad **[Dgo TecHub](https://dgotechub.org)** por el apoyo y el espacio de compartir con los demás.
- Compañeros de accountability por el feedback continuo
- Anthropic (Claude) como AI pair programming partner

---

**⭐ Si este proyecto te sirve de referencia, ¡dame una estrella en GitHub!**

---

📌 **Mes actual**: [Month 01 - Foundations](months/month-01-foundations/)