from sqlalchemy.orm import mapped_column, relationship, Mapped

from database.orm.base import Base


class OtherTable(Base):
    __tablename__ = 'other_table'

    id: Mapped[int] = mapped_column(primary_key=True)

    tags = relationship('RecursiveExample', back_populates='recursive_example')
