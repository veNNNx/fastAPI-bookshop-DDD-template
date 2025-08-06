# 🚀 FastAPI DDD Template

A clean FastAPI project template using **Domain-Driven Design (DDD)** architecture.

## Features

- **FastAPI** – high-performance async web framework
- **DDD structure** – separation of concerns via domain/infrastructure/api layers
- **Dependency Injection** – using `dependency-injector`
- **PostgreSQL** with **SQLAlchemy**
- **Testing** – backend unit tests and API integration tests
- **Poetry** – modern dependency and virtual environment management  
- **Pre-commit hooks** – automated code quality checks and formatting before commits  

## Dependency Management (Poetry)

This project uses [Poetry](https://python-poetry.org/) for dependency and virtual environment management.

### Install dependencies:

```bash
poetry install --no-root
```

## Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to automate code quality checks and enforce best practices before commits.

### Setup

To enable pre-commit hooks locally, run:

```bash
pre-commit install
```
