from typing import TypedDict

from server import app


class HealthCheckReturn(TypedDict):
    message: str


@app.get("/health")
def health_check() -> HealthCheckReturn:
    return {"message": 'ok'}
