import allure
import requests
from jsonschema import validate

from utils import allure_attach, logger


class PetApiMethods:
    def __init__(self, url):
        self.url = url

    def create_pet(self, body: dict, schema: dict):
        with allure.step('Отправить запрос на создание питомца'):
            response = requests.post(f"{self.url}/pet", json=body)
        with allure.step('Проверить ответ по схеме после создания питомца'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response

    def get_pet_by_id(self, pet_id, schema: dict):
        with allure.step('Отправить запрос на получение питомца'):
            response = requests.get(f"{self.url}/pet/{pet_id}")
        with allure.step('Проверить ответ по схеме после получения питомца'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response

    def update_pet(self, body: dict, schema: dict):
        with allure.step('Отправить запрос на обновление питомца'):
            response = requests.put(f"{self.url}/pet", json=body)
        with allure.step('Проверить ответ по схеме после обновления питомца'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response

    def delete_pet_by_id(self, pet_id, schema: dict):
        with allure.step('Отправить запрос на удаление питомца'):
            response = requests.delete(f"{self.url}/pet/{pet_id}")
        with allure.step('Проверить ответ по схеме после удаления питомца'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response
