import requests
from modules.configurations import HOLDER_URL

import pytest

from modules.holder import Holder


def test_holder_status_code():
    response = requests.get(url=HOLDER_URL + "posts/1")
    assert response.status_code == 200


def test_holder_model():
    response = requests.get(url=HOLDER_URL + "posts/1")
    post_model = Holder.model_validate(response.json())
    assert response.status_code == 200
    assert post_model


def test_holder_title():
    response = requests.get(url=HOLDER_URL + "posts/1")
    post_model = Holder.model_validate(response.json())
    assert response.status_code == 200
    assert post_model.title == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"


@pytest.mark.parametrize("id, email", [
    (1, "Eliseo@gardner.biz"),
    (2, "Jayne_Kuhic@sydney.com"),
    (3, "Nikita@garfield.biz"),
    (4, "Lew@alysha.tv"),
    (5, "Hayden@althea.biz")])
def test_holder_id_with_email(id, email):
    response = requests.get(url=HOLDER_URL + "posts/1/comments")
    assert response.status_code == 200
    assert response.json()[id - 1].get("id") == id and response.json()[id - 1].get("email") == email


@pytest.mark.parametrize("field, value", [
    ("postId", 1),
    ("id", 5),
    ("name", "vero eaque aliquid doloribus et culpa"),
    ("email", "Hayden@althea.biz"),
    ("body", "harum non quasi et ratione\ntempore iure ex voluptates in ratione"
             "\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et")])
def test_holder_id5_comment(field, value):
    response = requests.get(url=HOLDER_URL + "posts/1/comments")
    assert response.status_code == 200
    assert response.json()[4].get(field) == value
