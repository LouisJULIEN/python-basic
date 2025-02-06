from typing import Type

from flask import abort
from pydantic import BaseModel, ValidationError, ConfigDict


class ForbidExtraKey(BaseModel):
    model_config = ConfigDict(extra='forbid')


def validate_payload_or_400(payload: any, pydantic_checker: Type[BaseModel]):
    try:
        validated_payload = pydantic_checker.model_validate(payload, strict=True)
    except ValidationError as validation_errors:
        errors_formated = []
        for an_error in validation_errors.errors():
            del an_error['url']
            if 'ctx' in an_error:
                del an_error['ctx']

            errors_formated.append(an_error)
        abort(400, errors_formated)

    return validated_payload.model_dump(by_alias=True)