from pydantic import BaseModel, ConfigDict


class ForbidExtraKey(BaseModel):
    model_config = ConfigDict(extra='forbid')
