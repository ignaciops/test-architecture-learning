# Test Architecture Learning - Roadmap 2026

🚀 Mi proyecto de aprendizaje público: 12 meses aprendiendo sobre Test Architecture

---

## 🎯 Objetivo

Dominar test architecture a través de un roadmap estructurado que cubre:

| Mes | Tema | Status |
|-----|------|--------|
| 01 | Foundations + Hexagonal Architecture | 🚧 |
| 02 | Architecture Refinement + Microservices | ⏳ |
| 03 | Contract Testing | ⏳ |
| 04 | Observability | ⏳ |
| 05 | Test Data Management | ⏳ |
| 06 | CI/CD Avanzado | ⏳ |
| 07 | Performance Testing | ⏳ |
| 08 | Chaos Engineering | ⏳ |
| 09 | Security Testing | ⏳ |
| 10 | Accessibility Testing | ⏳ |
| 11 | Test Strategy + DORA Metrics | ⏳ |
| 12 | Capstone Project | ⏳ |

---

## 📁 Estructura del Proyecto
```
.
├── framework/       # Framework de testing (evoluciona mensualmente)
├── tests/           # Tests organizados por tipo y SUT
├── suts/            # Sistemas bajo prueba
├── docs/            # Documentación general
├── months/          # Documentación mensual
└── .github/         # CI/CD pipelines
```

Ver [estructura completa](docs/architecture/README.md)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.14+
- Docker
- Node.js (para el blog)

### Setup
```bash
# Clone repo
git clone <tu-repo>
cd test-architecture-learning

# Setup Python environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
playwright install --with-deps

# Verify setup
pytest tests/ --collect-only
```

### Run Tests
```bash
# Local (with browser visible)
pytest tests/e2e/blog/ --headed

# Local (headless)
pytest tests/e2e/blog/

# Docker
docker-compose up --build

# Generate Allure report
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

---

## 📚 Documentación

- **[Learning Journal](docs/learning-journal.md)** - Aprendizajes diarios/semanales
- **[Workflows](docs/workflows.md)** - Ritmos y procesos
- **[Architecture Decisions](docs/architecture/decisions.md)** - ADRs
- **[Monthly Retros](months/)** - Retrospectivas mensuales

---

## 🧪 Tech Stack

### Core
- **Language**: Python 3.14+
- **E2E Testing**: Playwright
- **Test Framework**: Pytest
- **Reporting**: Allure
- **Architecture**: Hexagonal (Ports & Adapters)

### Infrastructure
- **Containers**: Docker + docker-compose
- **CI/CD**: GitHub Actions
- **VCS**: Git + GitHub

### Por Agregar (Próximos Meses)
- Mes 2: HTTPX (API testing)
- Mes 3: Pact (contract testing)
- Mes 4: OpenTelemetry (observability)
- [Ver roadmap completo](docs/roadmap.md)

---

## 📊 Métricas Actuales

**Última actualización**: 1 Enero 2025

| Métrica | Valor |
|---------|-------|
| Tests E2E | 0 → 8 (target mes 1) |
| Tests API | 0 |
| Pipeline Time | N/A → <10 min (target) |
| Blog Posts | 0 → 1 (target mes 1) |
| Lightning Talks | 0 → 1 (target mes 1) |
| Commits | 0 |

---

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal, pero:

- ⭐ **Stars** son bienvenidas (motivación++)
- 💬 **Feedback** en [Discussions](../../discussions)
- 🐛 **Issues** si encuentras algo roto

---

## 📞 Sígueme

- **Blog**: [ignaciops.dev](https://ignaciops.dev)
- **LinkedIn**: [Ignacio PS](https://linkedin.com/in/ignaciops)
- **Twitter/X**: [@ignaciopsdev](https://x.com/ignaciopsdev)

---

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE)

---

## 🙏 Agradecimientos

- Comunidad [Dgo TecHub](https://dgotechub.org)


---

⭐ Si este proyecto te inspira, dame una estrella en GitHub!