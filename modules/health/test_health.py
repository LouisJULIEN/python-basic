from misc.testing_http import fast_api_test_client


def test_health():
    res = fast_api_test_client.get('/health')
    assert res.status_code == 200
