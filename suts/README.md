# Systems Under Test (SUTs)

Este proyecto prueba múltiples aplicaciones a lo largo del roadmap 2026. Los SUTs **NO** están incluidos en este repositorio - cada uno vive en su propio repo o se levanta vía Docker.

---

## 🎯 Filosofía

- **SUTs externos** (blog, Saleor, Juice Shop) → Repos separados, se clonan en paralelo
- **SUTs custom** (microservicios FastAPI) → Viven en este repo en `microservices/`
- **Ambientes locales primero** → Salvo el blog (estático, read-only)

---

## 📋 SUTs por Mes

| Mes | SUT | Stack | Tipo | Ubicación |
|-----|-----|-------|------|-----------|
| 1-3 | Blog Personal | Astro + Keystatic | Externo | Repo separado |
| 2-6 | Microservicios | FastAPI + PostgreSQL | Custom | `microservices/` |
| 5-12 | Saleor E-commerce | Django + GraphQL + React | Externo | Repo separado |
| 9 | OWASP Juice Shop | Node.js + Angular | Externo | Docker |

---

## 🌐 SUTs Detallados

### 1. Blog Personal (Mes 1-3)

**Información**:
- **Repo**: [ignaciops/ignaciopsdev-blog](https://github.com/ignaciops/ignaciopsdev-blog)
- **Stack**: Astro + Keystatic
- **URL prod**: https://ignaciops.dev
- **URL local**: http://localhost:4321
- **Tests**: `tests/` (Mes 1), `tests/e2e/blog/` (Mes 2+)

**Características**:
- ✅ Sitio estático (solo lectura)
- ✅ Tests corren contra **prod por default** (seguro, sin side effects)
- ✅ Puede correrse local opcionalmente

**Setup local** (opcional):
```bash
# En directorio paralelo (fuera de test-architecture-learning/)
cd ~/projects  # o donde tengas tus repos
git clone https://github.com/ignaciops/ignaciopsdev-blog.git blog
cd blog

# Install dependencies
npm install

# Run dev server
npm run dev
# → Blog en http://localhost:4321
```

**Correr tests**:
```bash
# Contra producción (default, no requiere setup)
cd ~/projects/test-architecture-learning
pytest tests/ -v

# Contra local (si levantaste el blog localmente)
BLOG_BASE_URL=http://localhost:4321 pytest tests/ -v
```

**Variables de entorno**:
- `BLOG_BASE_URL` - Default: `https://ignaciops.dev`

---

### 2. Microservicios FastAPI (Mes 2-6)

**Información**:
- **Ubicación**: `microservices/` (en este repo)
- **Stack**: FastAPI + PostgreSQL + Docker
- **URL local**: http://localhost:8000 (users), http://localhost:8001 (content)
- **Tests**: `tests/api/` (Mes 2+)

**Características**:
- ⚠️ Servicios con **escritura en BD** (nunca contra prod)
- ✅ Ambiente completamente dockerizado
- ✅ Seed data controlado
- ✅ **Testcontainers** para aislamiento de tests (Mes 2+)

**Setup**:
```bash
cd test-architecture-learning/microservices

# Levantar todos los servicios
docker-compose up -d

# Verificar que estén corriendo
curl http://localhost:8000/health  # users-service
curl http://localhost:8001/health  # content-service

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down

# Detener y limpiar datos
docker-compose down -v
```

**Correr tests**:
```bash
# Los tests usan Testcontainers (desde Mes 2) - levantan PostgreSQL automáticamente
pytest tests/api/ -v

# No requiere docker-compose up manual
# Cada test suite obtiene su propia BD limpia y aislada
```

**Variables de entorno**:
- `USERS_API_URL` - Default: `http://localhost:8000`
- `CONTENT_API_URL` - Default: `http://localhost:8001`

---

### 3. Saleor E-commerce (Mes 5-12)

**Información**:
- **Repo**: [saleor/saleor](https://github.com/saleor/saleor)
- **Stack**: Django + PostgreSQL + GraphQL + React Storefront
- **URL local API**: http://localhost:8000/graphql/
- **URL local Storefront**: http://localhost:3000
- **Tests**: `tests/e2e/saleor/`, `tests/api/saleor/`

**Características**:
- ⚠️ E-commerce completo (checkout, pagos, inventario)
- ⚠️ **NUNCA contra producción** (side effects graves)
- ✅ Setup dockerizado completo
- ✅ Seed data de productos/categorías

**Setup**:
```bash
# En directorio paralelo
cd ~/projects
git clone https://github.com/saleor/saleor.git
cd saleor

# Opción A: Docker (recomendado)
docker-compose up -d

# Opción B: Local (requiere Python + Node)
# Ver https://docs.saleor.io/docs/3.x/developer/getting-started/architecture

# Crear superuser
docker-compose exec api python manage.py createsuperuser

# Cargar datos de ejemplo
docker-compose exec api python manage.py populatedb

# Verificar
# API: http://localhost:8000/graphql/
# Dashboard: http://localhost:9000/
# Storefront: http://localhost:3000/
```

**Correr tests**:
```bash
# E2E contra storefront
pytest tests/e2e/saleor/ -v

# API tests (GraphQL)
pytest tests/api/saleor/ -v
```

**Variables de entorno**:
- `SALEOR_API_URL` - Default: `http://localhost:8000/graphql/`
- `SALEOR_STOREFRONT_URL` - Default: `http://localhost:3000`

---

### 4. OWASP Juice Shop (Mes 9)

**Información**:
- **Repo**: [juice-shop/juice-shop](https://github.com/juice-shop/juice-shop)
- **Stack**: Node.js + Angular + SQLite
- **URL local**: http://localhost:3000
- **Tests**: `tests/security/`

**Características**:
- 🔒 Aplicación **intencionalmente vulnerable** para security testing
- ⚠️ **Solo para aprendizaje** - contiene vulnerabilidades reales
- ✅ Setup con Docker en 1 comando

**Setup**:
```bash
# Opción A: Docker (más fácil)
docker run -d -p 3000:3000 bkimminich/juice-shop

# Opción B: Clonar repo
cd ~/projects
git clone https://github.com/juice-shop/juice-shop.git
cd juice-shop
npm install
npm start

# Verificar
# → http://localhost:3000
```

**Correr tests**:
```bash
# Security scanning (OWASP ZAP)
pytest tests/security/ -v

# SAST (Bandit, Semgrep) - contra el código de este repo
./security/sast/run-sast.sh
```

**Variables de entorno**:
- `JUICE_SHOP_URL` - Default: `http://localhost:3000`

---

## 🚀 Quick Reference

### Levantar todos los SUTs necesarios (ejemplo Mes 5)
```bash
# Terminal 1: Blog (si quieres testear local)
cd ~/projects/blog && npm run dev

# Terminal 2: Microservicios
cd ~/projects/test-architecture-learning/microservices
docker-compose up

# Terminal 3: Saleor
cd ~/projects/saleor
docker-compose up

# Terminal 4: Tests
cd ~/projects/test-architecture-learning
pytest tests/ -v
```

### Detener todo
```bash
# Microservicios
cd microservices && docker-compose down

# Saleor
cd ~/projects/saleor && docker-compose down

# Blog (Ctrl+C en terminal)

# Juice Shop
docker stop $(docker ps -q --filter ancestor=bkimminich/juice-shop)
```

---

## 📝 Notas Importantes

### Sobre ambientes de producción

- ✅ **Blog**: Seguro testear contra prod (estático, read-only)
- ❌ **Microservicios**: NUNCA contra prod (escribe en BD)
- ❌ **Saleor**: NUNCA contra prod (crea órdenes, modifica inventario)
- ❌ **Juice Shop**: No tiene ambiente prod (es para testing de seguridad)

### Sobre datos de prueba

Cada SUT tiene su estrategia de test data:

| SUT | Estrategia |
|-----|------------|
| Blog | Datos reales de producción (posts publicados) |
| Microservicios | Factories (Factory Boy + Faker) + Testcontainers |
| Saleor | Seed data (`populatedb`) + Factories |
| Juice Shop | Datos incluidos en la aplicación |

### Sobre persistencia

- **Blog**: No hay persistencia local (regenera en cada build)
- **Microservicios**:
  - Docker Compose: BD PostgreSQL en volumen (usar `docker-compose down -v` para limpiar)
  - Testcontainers (Mes 2+): BD temporal, se destruye automáticamente
- **Saleor**: BD PostgreSQL en Docker (volumen persistente)
- **Juice Shop**: SQLite en contenedor (se resetea al reiniciar)

---

## 🔧 Troubleshooting

### "pytest no encuentra los tests"
```bash
# Verifica que estés en el directorio correcto
cd test-architecture-learning
pwd  # Debe terminar en /test-architecture-learning

# Verifica que pytest esté instalado
pip list | grep pytest

# Re-instala si es necesario
pip install -e .
```

### "El blog local no carga"
```bash
# Verifica que Node esté instalado
node --version  # Debe ser 20+

# Reinstala dependencias
cd ~/projects/blog
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### "Microservicios no responden"
```bash
# Verifica que Docker esté corriendo
docker ps

# Revisa logs
cd microservices
docker-compose logs -f

# Reinicia servicios
docker-compose restart

# Si sigue fallando, reconstruye
docker-compose down -v
docker-compose up --build
```

### "Saleor tarda mucho en levantar"

Es normal, Saleor es complejo. Primera vez puede tomar 5-10 minutos.
```bash
# Ver progreso
docker-compose logs -f api

# Esperar a ver: "Listening at: http://0.0.0.0:8000"
```

---

## 📚 Recursos

- [Astro Docs](https://docs.astro.build/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Saleor Docs](https://docs.saleor.io/)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)

---

**Última actualización**: 3 Enero 2026