# TaskFlow API

Backend portfolio project by **Stefan Golubev** — an asynchronous REST API for personal task management.

## Tech stack
Python 3.12 · FastAPI · SQLAlchemy 2 · PostgreSQL · Pydantic · JWT · Alembic · Docker · pytest · GitHub Actions

## Implemented
- user registration and password hashing;
- JWT authentication;
- protected CRUD endpoints for personal tasks;
- task status filtering;
- asynchronous SQLAlchemy database access;
- PostgreSQL for Docker and SQLite fallback for local development/tests;
- Alembic database migrations;
- Swagger/OpenAPI documentation;
- unit tests and CI.

## API
| Method | Endpoint | Description |
| --- | --- | --- |
| POST | /auth/register | Create account |
| POST | /auth/login | Get JWT token |
| GET | /tasks | List user's tasks |
| POST | /tasks | Create task |
| PATCH | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |
| GET | /health | Health check |

## Run with Docker
```bash
cp .env.example .env
docker compose up --build
docker compose exec api alembic upgrade head
```
Swagger UI: `http://localhost:8000/docs`

## Tests
```bash
pytest -q
```

## Project structure
```text
app/          FastAPI application
app/routers/  HTTP endpoints
alembic/      database migrations
tests/        automated tests
```

The repository contains only example environment variables. Secrets and local `.env` files are ignored.
