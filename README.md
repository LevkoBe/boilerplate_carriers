# ShipEngine Carrier Service

FastAPI-based microservice implementing CRUD operations for carrier management, inspired by ShipEngine's API.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- Async/await throughout (FastAPI + SQLAlchemy 2.0 + asyncpg)
- Background task processing (ARQ)
- Transactional batch operations
- Database migrations (Alembic)
- Comprehensive test coverage

## Tech Stack

- **Python 3.10+**
- **FastAPI** - Modern async web framework
- **SQLAlchemy 2.0** - Async ORM
- **PostgreSQL** - Primary database
- **asyncpg** - Async Postgres driver
- **ARQ** - Async task queue (Redis-based)
- **Alembic** - Database migrations
- **Pytest** - Testing framework

## Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.10+

### Installation

1. Clone the repository:

```bash
git clone https://github.com/LevkoBe/boilerplate_carriers.git
cd boilerplate_carriers
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start infrastructure:

```bash
docker-compose up -d
```

4. Run migrations:

```bash
alembic upgrade head
```

5. Start the API server:

```bash
uvicorn src.main:app --reload
```

6. (Optional) Start background worker:

```bash
arq src.app.worker.WorkerSettings
```

### API Documentation

Open your browser to `http://localhost:8000/docs` for interactive Swagger UI.

## API Endpoints

### Carriers

- `GET /api/v1/carriers/` - List all carriers
- `POST /api/v1/carriers/` - Create new carrier
- `GET /api/v1/carriers/{id}` - Get carrier by ID
- `PUT /api/v1/carriers/{id}` - Update carrier
- `DELETE /api/v1/carriers/{id}` - Delete carrier
- `PATCH /api/v1/carriers/{id}/balance` - Update balance (triggers background task)
- `POST /api/v1/carriers/batch` - Create multiple carriers (transactional)

## Testing

Run the test suite:

```bash
# Create test database
createdb -U postgres ship_db_test

# Run tests
pytest tests/ -v
```

### Final Touches

Update `.env`:

```

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=ship_db

```
