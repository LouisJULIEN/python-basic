from typing import TypedDict

from modules.version.version import get_app_version
from server import app


class VersionReturn(TypedDict):
    version: str


@app.get("/version")
def version() -> VersionReturn:
    app_version = get_app_version()
    return {"version": app_version}
