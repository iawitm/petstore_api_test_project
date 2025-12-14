import os

import pytest
from dotenv import load_dotenv

from api.user import UserApiMethods
from helpers.helpers import load_json
from schemas.user_schemas import created_user, deleted_user


@pytest.fixture()
def api_url():
    load_dotenv()
    api_url = os.getenv("PETSTORE_API_URL")
    return  api_url

@pytest.fixture()
def pre_created_user(api_url):
    request_body = load_json("user1.json")
    UserApiMethods(url=api_url).create_user(body=request_body, schema=created_user)
    yield request_body


@pytest.fixture()
def delete_pre_created_user(api_url, pre_created_user):
    username = pre_created_user["username"]
    yield
    UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)
