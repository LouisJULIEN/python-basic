from typing import Type

from fastapi import HTTPException

from database.engine import PostgresSession
from database.orm import RecursiveExample, OtherTable


def get_or_404_entry(pg_session: PostgresSession, entry_id: int) -> Type[RecursiveExample]:
    found_entry = pg_session.get(RecursiveExample, entry_id)

    if found_entry is None:
        raise HTTPException(status_code=404)
    return found_entry


def create_entries(pg_session: PostgresSession, number_sub_tables: int) -> RecursiveExample:
    one_table = OtherTable()
    pg_session.add(one_table)
    pg_session.flush()  # to fetch the id value

    parent_recursive_table = RecursiveExample(
        category='hello',
        trait='it is me',
        other_table_id=one_table.id
    )
    pg_session.add(parent_recursive_table)
    pg_session.flush()  # to fetch the id value

    current_parent_id = parent_recursive_table.id

    for i in range(number_sub_tables - 1):
        one_recursive_table = RecursiveExample(
            category='hello',
            trait='it is me',
            trait_content_vector=[i],
            parent_tag_id=current_parent_id
        )
        pg_session.add(one_recursive_table)
        pg_session.flush()  # to fetch the id value
        current_parent_id = one_recursive_table.id

    return parent_recursive_table
