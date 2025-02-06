def test_version(flask_testing_client):
    res = flask_testing_client.get('/version', json=None)
    assert res.status_code == 200
    assert type(res.json['version']) is str
