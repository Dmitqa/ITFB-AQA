import pytest
import requests
from modules.configurations import DOG_URL
from modules.dog import Dog


def test_dog_status_code(get_dog_url):
    code = get_dog_url.status_code
    assert code == 200


def test_dog_model(get_dog_url):
    code = get_dog_url.status_code
    assert code == 200
    Dog.model_validate(get_dog_url.json())


def test_dog_status_field(get_dog_url):
    code = get_dog_url.status_code
    assert code == 200
    assert get_dog_url.json()["status"] == "success"


@pytest.mark.parametrize("breed", [
    "akita",
    "chippiparai",
    "kuvasz",
    "pitbull",
    "shihtzu"])
def test_dog_breeds_in_message(breed):
    response = requests.get(url=DOG_URL + "breeds/list/all")
    assert response.status_code == 200
    assert breed in response.json().get("message")


@pytest.mark.parametrize("terrier", [
    "cairn",
    "norwich",
    "russell",
    "toy",
    "wheaten"])
def test_dog_terrier(terrier):
    response = requests.get(url=DOG_URL + "breeds/list/all")
    assert response.status_code == 200
    assert terrier in response.json().get("message").get("terrier")
