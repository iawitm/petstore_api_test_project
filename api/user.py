import requests
from jsonschema import validate
import logging

class UserApiMethods:
    def __init__(self, url):
        self.url = url

    POST_CREATE_USER = '/user'

    def create_user(self, body: dict, schema: dict):

        response = requests.post(f"{self.url}{self.POST_CREATE_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response

    def get_user_by_username(self, username, schema: dict):
        response = requests.get(f"{self.url}/user/{username}")
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response

    def update_user_by_username(self, username, body: dict, schema: dict):
        response = requests.put(f"{self.url}/user/{username}", json=body)
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response

    def delete_user_by_username(self, username, schema: dict):
        response = requests.delete(f"{self.url}/user/{username}")
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response