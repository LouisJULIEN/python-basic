def test_version(flask_testing_client):
    res = flask_testing_client.get('/version')
    assert res.status_code == 200
    assert type(res.json['version']) is str

def test_monkeypatch_example(monkeypatch, flask_testing_client):
    monkeypatch.setattr('modules.version.version.get_app_version.__code__',
                        (lambda *_: '6.6.6-mocked').__code__)

    res = flask_testing_client.get('/version')

    assert res.status_code == 200
    assert res.json== {'version': '6.6.6-mocked'}