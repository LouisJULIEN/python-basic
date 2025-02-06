def test_entry_creation_payload(flask_testing_client):
    should_not_exist = flask_testing_client.get('/entry/0')
    assert should_not_exist.status_code == 404

    should_not_exist = flask_testing_client.post('/entry', json={'number_sub_tables': 2})
    assert should_not_exist.status_code == 200
    entries = should_not_exist.json['entries']
    assert entries['id'] is not None
    assert entries['childrenTags'][0]['traitContentVector'] == [0.0]
    created_entry_id = entries['id']
    print(created_entry_id)

    created_entry = flask_testing_client.get(f'/entry/{created_entry_id}')
    assert created_entry.status_code == 200
    assert  created_entry.json['entry']['id'] == created_entry_id


def test_check_payload_bad_request(flask_testing_client):
    res = flask_testing_client.post('/entry', json={'number_sub_tables': 0})
    assert res.status_code == 400

    res = flask_testing_client.post('/entry', json={})
    assert res.status_code == 400

    res = flask_testing_client.post('/entry', json={'number_sub_tables': 'i am string'})
    assert res.status_code == 400

    res = flask_testing_client.post('/entry', json={'number_sub_tables': 5, 'extra': "cheese"})
    assert res.status_code == 400
