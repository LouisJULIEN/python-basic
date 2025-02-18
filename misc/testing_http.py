from fastapi.testclient import TestClient

from server import app

fast_api_test_client = TestClient(app)
