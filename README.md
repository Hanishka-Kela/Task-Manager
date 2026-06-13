# Task Manager API

A multi-user Task Management REST API built with **FastAPI**, **SQLAlchemy 2.0**, and **JWT authentication**.

## Features

- 🔐 **JWT Authentication** — signup, login, and Bearer token-protected routes
- 👤 **Per-user task isolation** — users can only see and manage their own tasks
- ✅ **Full CRUD** — create, read, update status, and delete tasks
- 📋 **Confirm password validation** — enforced at signup via Pydantic
- 📖 **Interactive Swagger docs** — with one-click OAuth2 Authorize support
- 🗄️ **SQLite** — zero-config local database, auto-created on startup

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 (`Mapped` types) |
| Database | SQLite |
| Auth | JWT via PyJWT + passlib bcrypt |
| Validation | Pydantic v2 |
| Server | Uvicorn |
| Package Manager | uv |

---

## Project Structure

```
Task Manager/
├── app/
│   ├── main.py              # FastAPI app entry point & router registration
│   ├── database.py          # DB engine, session factory, Base
│   ├── models.py            # SQLAlchemy ORM models (User, Task)
│   ├── schemas.py           # Pydantic schemas (request/response DTOs)
│   ├── core/
│   │   └── security.py      # JWT config, password hashing, get_current_user
│   ├── repositories/
│   │   ├── user_repository.py   # User DB queries
│   │   └── tasks_repository.py  # Task DB queries (filtered by owner)
│   ├── services/
│   │   ├── auth_services.py     # Auth business logic (register, login, token)
│   │   └── tasks_service.py     # Task business logic + ownership checks
│   └── routers/
│       ├── auth_router.py       # /auth endpoints (signup, login, token)
│       └── tasks_router.py      # /tasks endpoints (protected)
├── pyproject.toml           # Project metadata & dependencies
├── pyrefly.toml             # Pyrefly type checker config
└── tasks.db                 # SQLite database (auto-created, git-ignored)
```

---

## Quickstart

### Prerequisites
- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

```bash
# Clone and enter the project
cd "Task Manager"

# Install dependencies
uv sync

# Start the server
uv run uvicorn app.main:app --reload
```

The database (`tasks.db`) is created automatically on first run.

---

## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/auth/signup` | Register a new user | No |
| `POST` | `/auth/login` | Login with JSON body, returns JWT | No |
| `POST` | `/auth/token` | Login with form data (for Swagger) | No |

### Tasks

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/tasks` | Create a new task | ✅ |
| `GET` | `/tasks` | Get all your tasks | ✅ |
| `GET` | `/tasks/{task_id}` | Get a specific task | ✅ |
| `PATCH` | `/tasks/{task_id}` | Update task status | ✅ |
| `DELETE` | `/tasks/{task_id}` | Delete a task | ✅ |

---


### Using Swagger UI
1. Open **http://127.0.0.1:8000/docs**
2. Click the 🔒 **Authorize** button
3. Enter your `username` and `password` → click **Authorize**
4. All protected endpoints will now automatically include your token

---