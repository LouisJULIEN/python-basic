import os


def is_local() -> bool:
    return ENVIRONMENT is None and (
            ('localhost' in POSTGRES_CONNECTION_STRING) or
            ('127.0.0.1' in POSTGRES_CONNECTION_STRING)
    )


def is_prod() -> bool:
    return ENVIRONMENT == 'production'

LOG_SQL_REQUEST = 'SQL' in os.environ
ENVIRONMENT = os.environ.get('ENVIRONMENT_BASIC_PYTHON')
POSTGRES_CONNECTION_STRING = os.environ.get(
    "POSTGRES_CONNECTION_STRING",
    "postgresql+psycopg2://postgres:@localhost:5432/basic_python"
)
