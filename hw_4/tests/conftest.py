import pytest
import requests

from modules.configurations import DOG_URL


@pytest.fixture
def get_dog_url():
    response = requests.get(url=DOG_URL + "breed/hound/list")
    return response


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/"
    ),

    parser.addoption(
        "--status_code",
        default=200
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_status_code(request):
    return request.config.getoption("--status_code")
