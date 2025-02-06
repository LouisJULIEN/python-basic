import json

with open("version.json") as fp:
    version_content = json.load(fp)
    app_version = version_content["version"]


def get_app_version() -> str:
    return app_version
