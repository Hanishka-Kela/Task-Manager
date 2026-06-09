# Task Manager

Lightweight Task Manager API built with FastAPI and SQLAlchemy.

## Overview

This project provides a simple backend API for managing tasks (create, read, update, delete) using FastAPI and SQLAlchemy. The codebase is minimal and intended as a starter template or learning example.

## Features

- REST API endpoints for task CRUD operations
- SQLAlchemy models and DB connection in `app/database.py` and `app/models.py`
- Pydantic schemas in `app/schemas.py`
- ASGI server entrypoint at `app/main.py`

## Requirements

- Python 3.14 or newer
- The project lists dependencies in `pyproject.toml` (FastAPI, SQLAlchemy, Uvicorn)

## Quickstart

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (using pip):

```bash
pip install -U pip
pip install "fastapi[standard]" sqlalchemy uvicorn
```

Alternatively, if you use a PEP 621 compatible installer, you can install from `pyproject.toml`:

```bash
pip install -e .
```

## Running the app

Run the app with Uvicorn from the project root:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open the interactive API docs at http://127.0.0.1:8000/docs

## Project layout

- `app/main.py` — FastAPI application and route registration
- `app/database.py` — database engine and session configuration
- `app/models.py` — SQLAlchemy ORM models
- `app/schemas.py` — Pydantic request/response schemas

## Database

The project uses SQLAlchemy for ORM. Configure your database connection URL in `app/database.py` (for example, using SQLite for local development). If the code uses an environment variable, set it prior to running the app.



