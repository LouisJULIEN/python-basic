from typing import Optional, List

from pgvector.sqlalchemy import Vector
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.orm.base import Base
from database.orm.other_table import OtherTable


class RecursiveExample(Base):
    __tablename__ = 'recursive_example'

    id: Mapped[int] = mapped_column(primary_key=True)

    other_table_id: Mapped[Optional[int]] = mapped_column(ForeignKey("other_table.id"), nullable=True)
    other_table: Mapped[OtherTable] = relationship(back_populates="tags")

    parent_tag_id: Mapped[Optional[int]] = mapped_column(ForeignKey("recursive_example.id"), nullable=True)
    parent_tag = relationship('RecursiveExample', back_populates='children_tags', remote_side=[id])
    children_tags = relationship('RecursiveExample', back_populates='parent_tag', remote_side=[parent_tag_id])

    category: Mapped[str] = mapped_column(Text(), nullable=False)
    trait: Mapped[str] = mapped_column(Text(), nullable=False)
    trait_content_vector: Mapped[Optional[List[float]]] = mapped_column(Vector, nullable=True)
