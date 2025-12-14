import os

import pytest
from dotenv import load_dotenv

from api.pet import PetApiMethods
from api.user import UserApiMethods
from helpers.json_helper import load_json
from schemas.pet_schemas import created_pet, deleted_pet
from schemas.user_schemas import created_user, deleted_user


@pytest.fixture()
def api_url():
    load_dotenv()
    api_url = os.getenv("PETSTORE_API_URL")
    return  api_url

@pytest.fixture()
def create_default_user(api_url):
    request_body = load_json("default_user.json")
    UserApiMethods(url=api_url).create_user(body=request_body, schema=created_user)
    yield request_body


@pytest.fixture()
def delete_default_user(api_url, create_default_user):
    username = create_default_user["username"]
    yield
    UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)

@pytest.fixture()
def create_default_pet(api_url):
    request_body = load_json("default_pet.json")
    PetApiMethods(url=api_url).create_pet(body=request_body, schema=created_pet)
    yield request_body

@pytest.fixture()
def delete_default_pet(api_url, create_default_pet):
    pet_id = create_default_pet["id"]
    yield
    PetApiMethods(url=api_url).delete_pet_by_id(pet_id, schema=deleted_pet)
