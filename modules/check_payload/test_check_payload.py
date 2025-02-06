def test_check_payload(flask_testing_client):
    res = flask_testing_client.post('/check', json={'works': True})
    assert res.status_code == 200


def test_check_payload_bad_request(flask_testing_client):
    res = flask_testing_client.post('/check', json={})
    assert res.status_code == 400

    res = flask_testing_client.post('/check', json={'works': 13})
    assert res.status_code == 400

    res = flask_testing_client.post('/check', json={'works': True, 'extra': "cheese"})
    assert res.status_code == 400

