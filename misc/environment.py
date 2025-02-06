import os

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")


def is_local() -> bool:
    return True
