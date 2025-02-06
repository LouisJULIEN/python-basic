import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from misc.environment import POSTGRES_CONNECTION_STRING, LOG_SQL_REQUEST
from misc.logger import logger

PostgresSession = Session

engine = create_engine(POSTGRES_CONNECTION_STRING)

if LOG_SQL_REQUEST:
    logger.warn('logging all SQL')
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def get_new_postgres_session(expire_on_commit=True) -> Session:
    return Session(engine, expire_on_commit=expire_on_commit)
