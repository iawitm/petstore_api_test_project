import json
from pathlib import Path

import requests
from jsonschema import validate

from api.user import UserApiMethods
from helpers.helpers import load_json
from resources import json_api
from schemas.user_schemas import created_user

URL = "https://petstore.swagger.io/v2"



def test_get_not_existing_user():
    requests.delete(f"{URL}/user/TestUsername")

    response = requests.get(f"{URL}/user/TestUsername")
    body = response.json()

    assert response.status_code == 404
    assert body["message"] == "User not found"

def test_delete_not_existing_user():
    requests.delete(f"{URL}/user/TestUsername")
    response = requests.delete(f"{URL}/user/TestUsername")
    assert response.status_code == 404
    assert response.headers["Content-Length"] == '0'

def test_create_pet():
    response = requests.post(f"{URL}/pet", json={
  "id": 5443332222,
  "category": {
    "id": 1,
    "name": "cat"
  },
  "name": "Joe",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "cute"
    }
  ],
  "status": "available"
})

    assert response.status_code == 200
    assert response.json()["id"] == 5443332222
    assert response.json()["category"]["name"] == "cat"
    assert response.json()["name"] == "Joe"

def test_get_pet():
    response = requests.get(f"{URL}/pet/5443332222")
    assert response.status_code == 200
    assert response.json()["id"] == 5443332222
    assert response.json()["category"]["name"] == "cat"
    assert response.json()["name"] == "Joe"

def test_update_pet():
    requests.post(f"{URL}/pet", json={
  "id": 5443332222,
  "category": {
    "id": 1,
    "name": "cat"
  },
  "name": "Joe",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "cute"
    }
  ],
  "status": "available"
})
    response = requests.put(f"{URL}/pet", json={
  "id": 5443332222,
  "category": {
    "id": 1,
    "name": "dog"
  },
  "name": "Jack",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "haunting"
    }
  ],
  "status": "available"
})

    response_get = requests.get(f"{URL}/pet/5443332222")
    body_get = response_get.json()

    assert response.status_code == 200
    assert body_get["id"] == 5443332222
    assert body_get["category"]["name"] == "dog"
    assert body_get["name"] == "Jack"

def test_delete_pet():
    requests.post(f"{URL}/pet", json={
  "id": 5443332222,
  "category": {
    "id": 1,
    "name": "cat"
  },
  "name": "Joe",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "cute"
    }
  ],
  "status": "available"
})
    response = requests.delete(f"{URL}/pet/5443332222")
    body = response.json()
    assert response.status_code == 200
    assert body["message"] == "5443332222"

def test_get_not_existing_pet():
    requests.delete(f"{URL}/pet/5443332222")
    response = requests.get(f"{URL}/pet/5443332222")
    body = response.json()
    assert response.status_code == 404
    assert body["message"] == "Pet not found"

def test_delete_not_existing_pet():
    requests.delete(f"{URL}/pet/5443332222")
    response = requests.delete(f"{URL}/pet/5443332222")
    assert response.status_code == 404
    assert response.headers["Content-Length"] == '0'
