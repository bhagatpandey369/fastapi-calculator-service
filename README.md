# FastAPI Calculator Service

This is a simple calculator microservice built with FastAPI. It supports addition, subtraction, multiplication, and division via POST endpoints.

## Features

- RESTful API for basic math operations
- Environment variable configuration
- Docker-ready
- Unit tested with `pytest`
- CI pipeline via GitHub Actions

## How to Run

### Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
