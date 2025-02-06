import pytest


@pytest.fixture()
def flask_testing_app():
    from server import app
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def flask_testing_client(flask_testing_app):
    return flask_testing_app.test_client()
