# Recursos de Aprendizaje: Test Architecture
## Libros

### Obligatorios (Inversión: ~$150 USD)

| Libro | Autor | Precio | Mes de Uso | Por Qué |
|-------|-------|--------|------------|---------|
| **Python Testing with pytest** 2nd ed | Brian Okken | ~$35 | Mes 1 | Fundamento de todo el framework |
| **Clean Architecture** | Robert Martin | ~$40 | Mes 2 | Patrones arquitectónicos |
| **Observability Engineering** | Charity Majors et al. | ~$50 | Mes 4 | Tracing y debugging |
| **Accelerate** | Forsgren, Humble, Kim | ~$25 | Mes 11 | DORA metrics y estrategia |

### O'Reilly - Directamente Aplicables al Roadmap

| Libro | Autor | Mes de Uso | Por Qué | Prioridad |
|-------|-------|------------|---------|-----------|
| **Architecture Patterns with Python** | Percival & Gregory | Mes 1-2 | Implementación hexagonal EN PYTHON | ⭐⭐⭐ CRÍTICO |
| **Building Microservices** 2nd ed | Sam Newman | Mes 2-3 | Microservices + Contract Testing | ⭐⭐⭐ |
| **Monolith to Microservices** | Sam Newman | Mes 2-3 | Patrones de descomposición | ⭐⭐ |
| **Fundamentals of Software Architecture** 2nd ed | Richards & Ford | Mes 2, 11-12 | Base teórica, ADRs, trade-offs | ⭐⭐⭐ |
| **Building Evolutionary Architectures** 2nd ed | Ford et al. | Mes 6, 11 | Fitness functions (¡son tests!) | ⭐⭐ |

### O'Reilly - Complementarios (Lectura Selectiva)

| Libro | Capítulos Útiles | Mes de Uso | Por Qué |
|-------|------------------|------------|---------|
| **Software Architecture: The Hard Parts** | Cap. sobre service boundaries | Mes 2-3 | Trade-offs en arquitectura distribuida |
| **Learning Domain-Driven Design** | Cap. sobre Bounded Contexts, Entities | Mes 2, 5 | Diseño de scenarios y factories |
| **Communication Patterns** | Patrones síncronos/asíncronos | Mes 3-4 | Contract testing + observability |
| **Designing Distributed Systems** 2nd ed | Patrones de resiliencia | Mes 4, 8 | Observability + Chaos Engineering |
| **Foundations of Scalable Systems** | Patrones de escalabilidad | Mes 7 | Performance testing strategy |

### Recomendados (Opcionales)

| Libro | Autor | Precio | Por Qué |
|-------|-------|--------|---------|
| Release It! | Michael Nygard | ~$45 | Production systems + resilience patterns |
| Chaos Engineering | Rosenthal & Jones | ~$45 | Mes 8 - Chaos |
| The Web Application Hacker's Handbook | Stuttard & Pinto | ~$50 | Security (muy denso) |
| Staff Engineer | Will Larson | ~$30 | Career growth |
| The Pragmatic Programmer | Hunt & Thomas | ~$50 | General wisdom |

---

## Recursos por Mes

### Mes 1: Playwright + Arquitectura Hexagonal Básica

**Libros**
1. **Architecture Patterns with Python** - Capítulos 1-7
   - Cap 1-4: Domain Modeling, Repository, Abstractions, Service Layer
   - Cap 5-7: TDD, Unit of Work, Aggregates

2. **Python Testing with pytest** - Capítulos 1-5
   - Fixtures, conftest.py, parametrización

**Documentación Oficial (Gratis)**
- [Playwright Python Docs](https://playwright.dev/python/)
  - Sección: Locators
  - Sección: Best Practices
- [Testcontainers Python Docs](https://testcontainers-python.readthedocs.io/)
- [Allure Pytest Docs](https://docs.qameta.io/allure-report/)

**Videos (Gratis)**
- "Playwright Python" - Valentín Despa (YouTube)
- "Testcontainers Tutorial" - AtomicJar (YouTube)

**Artículos**
- Martin Fowler: "PageObject"
- "The Journey Pattern" - Tom Carver
- "Beyond Page Objects" - Angie Jones (InfoQ)

---

### Mes 2: Arquitectura Limpia + Microservicios

**Libros**
1. **Clean Architecture** - Completo
   - Principios SOLID
   - Reglas de dependencia
   - Casos de uso

2. **Fundamentals of Software Architecture** - Capítulos 1-10
   - Cap 1-5: Fundamentos, estilos arquitectónicos
   - Cap 9-10: Foundations (para ADRs)

3. **Building Microservices 2nd ed** - Capítulos 1-4, 9-10
   - Cap 1-4: Microservices intro, modeling, splitting
   - Cap 9-10: Testing, monitoring

4. **Architecture Patterns with Python** - Repaso y aplicación

**Documentación (Gratis)**
- [Allure Python Examples](https://github.com/allure-framework/allure-python)
- [FastAPI Docs](https://fastapi.tiangolo.com/)

**Videos (Gratis)**
- "Beyond Page Objects" - Angie Jones (YouTube)
- "Clean Architecture in Testing" - varios en YouTube

**Artículos (Gratis)**
- "Hexagonal Architecture in Test Automation" - Medium

---

### Mes 3: Contract Testing

**Libros**
1. **Building Microservices 2nd ed** - Capítulos 7, 9
   - Cap 7: Communication patterns
   - Cap 9: Testing (consumer-driven contracts)

2. **Monolith to Microservices** - Capítulos 4-5
   - Cap 4-5: Breaking apart, data decomposition

3. **Communication Patterns** - Capítulos sobre sync/async patterns (opcional)

**Documentación Oficial (Gratis)**
- [Pact Python Workshop](https://docs.pact.io/getting_started/workshops/python)
- [Pact Python Examples](https://github.com/pact-foundation/pact-python)
- [WireMock Docs](https://wiremock.org/docs/)

**Videos (Gratis)**
- "Consumer-Driven Contracts" - Matt Fellows (YouTube)
- "Pact Tutorial" - PactFlow (YouTube)

**Artículos (Gratis)**
- Martin Fowler: "Testing Strategies in a Microservice Architecture"
- "Contract Testing vs Integration Testing" - PactFlow Blog

---

### Mes 4: Observabilidad

**Libros**
1. **Observability Engineering** - Completo
   - Todo el libro es relevante
   - Focus en distributed tracing

2. **Designing Distributed Systems 2nd ed** - Capítulos sobre observability (opcional)

**Documentación Oficial (Gratis)**
- [OpenTelemetry Python Docs](https://opentelemetry.io/docs/languages/python/)
- [Grafana Tempo Docs](https://grafana.com/docs/tempo/)
- [Grafana Loki Docs](https://grafana.com/docs/loki/)

**Cursos (Gratis)**
- "Distributed Tracing with Tempo" - Grafana Labs
- [OpenTelemetry Bootcamp](https://www.youtube.com/playlist?list=PLVlVJVhLBVD0nR9IJ3aIdwvxz2BoL8r-F) - YouTube

---

### Mes 5: Test Data Management

**Libros**
1. **Learning Domain-Driven Design** - Capítulos 2-4 (opcional)
   - Cap 2: Discovering domain knowledge
   - Cap 3-4: Managing domain complexity, Entities
   - Útil para diseñar factories que representen el dominio

**Documentación (Gratis)**
- [Factory Boy Docs](https://factoryboy.readthedocs.io/)
- [Faker Docs](https://faker.readthedocs.io/)
- [Saleor Docs](https://docs.saleor.io/)

**Artículos (Gratis)**
- "Testcontainers Best Practices" - AtomicJar Blog
- "Test Data Management Strategies" - Ministry of Testing

---

### Mes 6: CI/CD Avanzado

**Libros**
1. **Building Evolutionary Architectures 2nd ed** - Capítulos 4-6
   - Cap 4-6: Fitness functions, evolutionary data, CI/CD
   - Fitness functions = automated tests

2. **Fundamentals of Software Architecture** - Capítulo 20
   - Analyzing architecture tradeoffs

**Documentación (Gratis)**
- [pytest-xdist Docs](https://pytest-xdist.readthedocs.io/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [SonarQube Docs](https://docs.sonarqube.org/)

**Videos (Gratis)**
- "Advanced GitHub Actions" - GitHub (YouTube)
- "CI/CD Best Practices" - varios

---

### Mes 7: Performance Testing

**Libros**
1. **Foundations of Scalable Systems** - Capítulos sobre performance (opcional)
   - Scalability patterns
   - Performance testing

2. **Release It!** - Capítulos 4-6 (opcional)
   - Stability patterns
   - Performance antipatterns

**Documentación Oficial (Gratis)**
- [k6 Learn Portal](https://k6.io/docs/)
- [k6 Examples](https://github.com/grafana/k6/tree/master/examples)

**Cursos (Gratis)**
- "Performance Testing with k6" - Test Automation University
- "k6 Office Hours" - Grafana (YouTube)

---

### Mes 8: Chaos Engineering

**Libros**
1. **Designing Distributed Systems 2nd ed** - Capítulos sobre resilience (opcional)
   - Patterns for resiliency

2. **Release It!** - Capítulos 4-5 (opcional)
   - Stability patterns

**Documentación (Gratis)**
- [Chaos Toolkit Docs](https://chaostoolkit.org/)
- [Toxiproxy Docs](https://github.com/Shopify/toxiproxy)

**Libros (Parcialmente Gratis)**
- "Chaos Engineering" - O'Reilly (primeros 3 capítulos gratis)

---

### Mes 9: Security Testing

**Documentación (Gratis)**
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP ZAP Docs](https://www.zaproxy.org/docs/)
- [Bandit Docs](https://bandit.readthedocs.io/)
- [Semgrep Docs](https://semgrep.dev/docs/)

**Cursos (Gratis)**
- "ZAP in Ten" - OWASP (YouTube series)

---

### Mes 10: Accessibility Testing

**Documentación (Gratis)**
- [axe-core Docs](https://www.deque.com/axe/)
- [Playwright Accessibility](https://playwright.dev/docs/accessibility-testing)
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [Pa11y Docs](https://pa11y.org/)

**Cursos (Gratis)**
- [Deque University](https://dequeuniversity.com/) - Algunos cursos gratuitos
- "Web Accessibility" - Google (Udacity, gratis)

---

### Mes 11: Estrategia y DORA

**Libros**
1. **Accelerate** - Completo
   - Todo el libro
   - Base para DORA metrics

2. **Fundamentals of Software Architecture** - Capítulos 19-21
   - Architecture decisions, risk, diagramming
   - Para Test strategy document y ADRs finales

3. **Building Evolutionary Architectures** - Capítulos 7-9
   - Putting it all together, organizational factors

**Documentación (Gratis)**
- [Google DORA Research](https://dora.dev/)
- [State of DevOps Report](https://cloud.google.com/devops/state-of-devops)
- [Ministry of Testing Templates](https://www.ministryoftesting.com/)

**Artículos (Gratis)**
- "How to calculate ROI of Test Automation" - varios

---

### Mes 12: Capstone + Consolidación

**Focus**:
- C4 diagrams
- ADRs finales
- Test strategy document
- Retrospectiva del año
- Consolidar aprendizajes en documentación

---

## Recursos Generales (Todo el Año)

### Fundamentos de CS (Opcional pero Recomendado)

**Cursos (Gratis)**
- [CS50 Introduction to Computer Science](https://cs50.harvard.edu/x/)
  - Lectures 0, 1, 3, 5 para data structures
- [Missing Semester of CS Education (MIT)](https://missing.csail.mit.edu/)
  - Shell, Git, debugging, security

**Repositorios de Referencia**
- [System Design Primer](https://github.com/donnemartin/system-design-primer)

### Blogs y Newsletters

- [Ministry of Testing](https://www.ministryoftesting.com/)
- [Test Guild](https://testguild.com/)
- [Automation Panda](https://automationpanda.com/)
- [Google Testing Blog](https://testing.googleblog.com/)
- [Martin Fowler's Blog](https://martinfowler.com/)

### Comunidades

- Ministry of Testing Slack
- Test Automation University Community
- r/QualityAssurance (Reddit)
- r/softwaretesting (Reddit)

### YouTube Channels

- Playwright Official
- Test Automation University
- Automation Step by Step
- Dave Farley (Continuous Delivery)
- Grafana Labs

---

## Resumen de Inversión

### Libros
| Categoría | Costo Aprox. |
|-----------|--------------|
| Obligatorios | ~$150 USD |
| Bundle O'Reilly | ~$25 USD* |
| Opcionales | ~$175 USD |

*Los bundles de Humble Bundle ofrecen excelente relación costo-beneficio

### Herramientas (Todas Gratuitas)
- VS Code + extensiones
- Docker Desktop
- Todas las herramientas del plan son OSS o tienen free tier

### Infraestructura
- VPS o servicios cloud según preferencia
- Dominio (opcional)

### Total Estimado: ~$175-350 USD
(Dependiendo de libros opcionales y si aprovechas bundles)

---

## Notas sobre Libros

### Prioridad de Lectura Sugerida

**Críticos** (lectura completa recomendada):
- Architecture Patterns with Python
- Python Testing with pytest
- Clean Architecture
- Fundamentals of Software Architecture
- Building Microservices 2nd ed
- Observability Engineering
- Accelerate

**Complementarios** (lectura selectiva por capítulos):
- Monolith to Microservices
- Building Evolutionary Architectures
- Software Architecture: The Hard Parts
- Learning Domain-Driven Design
- Communication Patterns
- Designing Distributed Systems
- Foundations of Scalable Systems

**Opcionales** (según interés personal):
- Release It!
- Chaos Engineering
- The Web Application Hacker's Handbook
- The Pragmatic Programmer
- Staff Engineer

### Estrategia de Lectura

- No es necesario leer todo linealmente
- Lee capítulos relevantes cuando los necesites en tu mes correspondiente
- Toma notas de conceptos clave
- Aplica cada concepto inmediatamente en código
- Es mejor profundizar en menos libros que superficializar muchos