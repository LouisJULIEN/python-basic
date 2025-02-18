import pytest

from misc.testing_http import fast_api_test_client


def test_entry_creation_payload():
    should_not_exist = fast_api_test_client.get('/entry/0')
    assert should_not_exist.status_code == 404

    should_not_exist = fast_api_test_client.post('/entry', json={'number_sub_tables': 2})
    assert should_not_exist.status_code == 200
    entries = should_not_exist.json()['entries']
    assert entries['id'] is not None
    assert entries['childrenTags'][0]['traitContentVector'] == [0.0]
    created_entry_id = entries['id']

    created_entry = fast_api_test_client.get(f'/entry/{created_entry_id}')
    assert created_entry.status_code == 200
    assert created_entry.json()['entry']['id'] == created_entry_id


errors_400 = [
    ({}, 400),
    ({'number_sub_tables': 0}, 400),
    ({'number_sub_tables': 'i am string'}, 400),
    ({'number_sub_tables': 5, 'extra': "cheese"}, 400),
]


@pytest.mark.parametrize("body, expected_status", errors_400)
def test_check_payload_bad_request(body, expected_status):
    res = fast_api_test_client.post('/entry', json=body)
    print(res.json())
    assert res.status_code == expected_status
