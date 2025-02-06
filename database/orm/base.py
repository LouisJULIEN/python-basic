from datetime import datetime
from typing import List, Optional

import numpy as np
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    to_dict_excluded_attributes: List[str] = ['created_at', 'updated_at']

    def to_dict(self,
                excluded_attributes: Optional[List[str]] = None, extra_attributes: Optional[List[str]] = None):
        excluded_attributes = self.to_dict_excluded_attributes if excluded_attributes is None else excluded_attributes
        extra_attributes = extra_attributes or []

        table_extra_attributes = {
            name: getattr(self, name) for name in extra_attributes
        }
        table_field_only_dict = {
            field.name: getattr(self, field.name)
            for field in self.__table__.c
            if field.name not in excluded_attributes
        }

        return {
            **table_extra_attributes,
            **table_field_only_dict
        }

    @staticmethod
    def _to_camel_case(snake_str: str):
        return "".join(x.capitalize() for x in snake_str.lower().split("_"))

    @staticmethod
    def _to_lower_camel_case(snake_str: str):
        # We capitalize the first letter of each component except the first one
        # with the 'capitalize' method and join them together.
        camel_string = Base._to_camel_case(snake_str)
        return snake_str[0].lower() + camel_string[1:]

    def to_json(self,
                excluded_attributes: Optional[List[str]] = None, extra_attributes: Optional[List[str]] = None):
        snake_case = self.to_dict(excluded_attributes=excluded_attributes, extra_attributes=extra_attributes)
        camel_dict = {Base._to_lower_camel_case(key): value for key, value in snake_case.items()}

        def specific_instances_to_list(obj):
            if isinstance(obj, np.ndarray):
                return specific_instances_to_list(obj.tolist())
            if isinstance(obj, dict):
                return {k: specific_instances_to_list(v) for k, v in obj.items()}
            if isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], Base):
                return [o.to_json() for o in obj]
            return obj

        json_ready_dict = {k: specific_instances_to_list(v) for k, v in camel_dict.items()}

        return json_ready_dict
