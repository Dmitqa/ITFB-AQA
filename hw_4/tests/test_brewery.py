import pytest
import requests
from modules.configurations import BREW_URL
from modules.brewery import Brewery


def test_brewery_status_code():
    response = requests.get(url=BREW_URL + "v1/breweries/936c3d7e-5d54-4459-b72c-117cdda059b4")
    assert response.status_code == 200


def test_brewery_schema():
    response = requests.get(url=BREW_URL + "v1/breweries/936c3d7e-5d54-4459-b72c-117cdda059b4")
    post_model = Brewery.model_validate(response.json())
    post_schema = {'id': {'title': 'Id', 'type': 'string'},
                   'name': {'title': 'Name', 'type': 'string'},
                   'brewery_type': {'title': 'Brewery Type', 'type': 'string'},
                   'address_1': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'title': 'Address 1'},
                   'address_2': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'title': 'Address 2'},
                   'address_3': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'title': 'Address 3'},
                   'city': {'title': 'City', 'type': 'string'},
                   'state_province': {'title': 'State Province', 'type': 'string'},
                   'postal_code': {'title': 'Postal Code', 'type': 'string'},
                   'country': {'title': 'Country', 'type': 'string'},
                   'longitude': {'title': 'Longitude', 'type': 'string'},
                   'latitude': {'title': 'Latitude', 'type': 'string'},
                   'phone': {'title': 'Phone', 'type': 'string'},
                   'website_url': {'title': 'Website Url', 'type': 'string'},
                   'state': {'title': 'State', 'type': 'string'},
                   'street': {'title': 'Street', 'type': 'string'}}

    assert post_model.model_json_schema().get("properties") == post_schema


def test_brewery_encoding():
    response = requests.get(url=BREW_URL + "v1/breweries/936c3d7e-5d54-4459-b72c-117cdda059b4")
    assert response.encoding == 'utf-8'


@pytest.mark.parametrize("index, field_name", [
    (1, "name"),
    (14, "city"),
    (26, "longitude"),
    (34, "state"),
    (41, "street")])
def test_brewery_geo(index, field_name):
    response = requests.get(url=BREW_URL + "v1/breweries")
    assert field_name in response.json()[index]


@pytest.mark.parametrize("field, value", [
    ("city", "Portland"),
    ("state_province", "Oregon"),
    ("postal_code", "97202-5518"),
    ("country", "United States")])
def test_brewery_area(field, value):
    response = requests.get(url=BREW_URL + "v1/breweries/936c3d7e-5d54-4459-b72c-117cdda059b4")
    assert response.json().get(field) == value
