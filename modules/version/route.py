from modules.version.version import get_app_version
from server import app


@app.get("/version")
def version():
    app_version = get_app_version()
    return {"version": app_version}
