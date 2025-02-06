# Basic Python

A basic Python web server with the ready-to-use boilerplate:
- Flask server
- Payload check with pydantic
- pytest tests with Flask route testing and monkeypatch example
- PostgresSQL ORM and migration with SQLAchemy and Alembic. Includes pgvector
- Ready to build Docker image
- Basic routes: healthcheck, version, CRUD example
- Autoreload of changes during development  

# Usage
## Setup
```bash
pip3 install -r requirements.txt
psql -c 'CREATE DATABASE python_basic'
alembic upgrade head
```

## Run
```bash
python3 server.py
```

## Test

Make sure that your working directory is this repository's root
```bash
pytest
```

## Postgresql migrations
Make sure your tables models are imported in [__init__.py](database/orm/__init__.py)
```bash
# Create a new migration file using autogenerate
alembic revision --autogenerate -m "update XXXXXXXXX"

# Migrate database
alembic upgrade head
```
## Add route
Follows [server.py](server.py) at line 14

## Docker

```bash
docker build -t python-basic/build . 

docker run -p 5000:5000 python-basic/build:latest
```
