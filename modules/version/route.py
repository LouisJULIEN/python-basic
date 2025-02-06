from modules.version.version import app_version
from server import app


@app.route("/version")
def version():
    return {"version": app_version}
