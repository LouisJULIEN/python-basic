from pydantic import Field

from database.engine import get_new_postgres_session
from misc.payload_validation import ForbidExtraKey
from modules.entry.service import create_entries, get_or_404_entry
from server import app


class HealthCheckPayload(ForbidExtraKey):
    number_sub_tables: int = Field(ge=1, le=5)


@app.post("/entry")
def create_database_entry(payload: HealthCheckPayload):
    pg_session = get_new_postgres_session()
    created_entries = create_entries(pg_session, payload.number_sub_tables)
    pg_session.commit()

    return {"entries": created_entries.to_json(extra_attributes=['children_tags'])}


@app.get("/entry/{entry_id}")
def get_database_entry(entry_id: int):
    pg_session = get_new_postgres_session()
    found_entry = get_or_404_entry(pg_session, entry_id)
    pg_session.commit()

    return {"entry": found_entry.to_json()}
