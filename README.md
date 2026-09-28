# TaskFlow API

Portfolio backend project by **Stefan Golubev**: an asynchronous REST API for personal task management.

## Stack
Python 3.12, FastAPI, PostgreSQL, SQLAlchemy 2, Pydantic, JWT, Docker, pytest.

## Features
- registration and JWT authentication;
- CRUD for personal tasks;
- task status filtering;
- async database access;
- Swagger/OpenAPI documentation;
- Docker Compose environment;
- automated health test.

## Run with Docker
```bash
cp .env.example .env
docker compose up --build
```
Open `http://localhost:8000/docs`.

## Tests
```bash
pytest
```
