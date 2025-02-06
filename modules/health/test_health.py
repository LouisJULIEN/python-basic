def test_health(flask_testing_client):
    res = flask_testing_client.get('/health', json=None)
    assert res.status_code == 200
