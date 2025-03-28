import pytest
import requests
from modules.configurations import DOG_URL
from modules.dog import Dog


def test_dog_status_code(get_dog_url):
    assert get_dog_url.status_code == 200


def test_dog_schema(get_dog_url):
    post_model = Dog.model_validate(get_dog_url.json())
    post_schema = {'message': {'items': {}, 'title': 'Message', 'type': 'array'},
                   'status': {'title': 'Status', 'type': 'string'}}

    assert post_model.model_json_schema().get("properties") == post_schema


def test_dog_status_field(get_dog_url):
    assert get_dog_url.json()["status"] == "success"


@pytest.mark.parametrize("breed", [
    "akita",
    "chippiparai",
    "kuvasz",
    "pitbull",
    "shihtzu"])
def test_dog_breeds_in_message(breed):
    response = requests.get(url=DOG_URL + "breeds/list/all")
    assert breed in response.json().get("message")


@pytest.mark.parametrize("terrier", [
    "cairn",
    "norwich",
    "russell",
    "toy",
    "wheaten"])
def test_dog_terrier(terrier):
    response = requests.get(url=DOG_URL + "breeds/list/all")
    assert terrier in response.json().get("message").get("terrier")
