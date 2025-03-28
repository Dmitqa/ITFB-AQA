import requests


def test_addoption(base_url, request_status_code):
    target = requests.get(url=base_url)
    assert target.status_code == request_status_code
