import requests
from jsonschema import validate
import logging

class PetApiMethods:
    def __init__(self, url):
        self.url = url

    def create_pet(self, body: dict, schema: dict):
        response = requests.post(f"{self.url}/pet", json=body)
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response

    def delete_pet_by_id(self, pet_id, schema: dict):
        response = requests.delete(f"{self.url}/pet/{pet_id}")
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response

    def get_pet_by_id(self, pet_id, schema: dict):
        response = requests.get(f"{self.url}/pet/{pet_id}")
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response

    def update_pet(self, body: dict, schema: dict):
        response = requests.put(f"{self.url}/pet", json=body)
        validate(instance=response.json(), schema=schema)
        logging.info(response.text)
        return response