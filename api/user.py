import allure
import requests
from jsonschema import validate

from utils import allure_attach, logger


class UserApiMethods:
    def __init__(self, url):
        self.url = url

    def create_user(self, body: dict, schema: dict):
        with allure.step('Отправить запрос на создание пользователя'):
            response = requests.post(f"{self.url}/user", json=body)
        with allure.step('Проверить ответ по схеме после создания пользователя'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response

    def get_user_by_username(self, username, schema: dict):
        with allure.step('Отправит запрос на получение пользователя'):
            response = requests.get(f"{self.url}/user/{username}")
        with allure.step('Проверить ответ по схеме после получения пользователя'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response

    def update_user_by_username(self, username, body: dict, schema: dict):
        with allure.step('Отправить запрос на обновление пользователя'):
            response = requests.put(f"{self.url}/user/{username}", json=body)
        with allure.step('Проверить ответ по схеме после обновления пользователя'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response

    def delete_user_by_username(self, username, schema: dict):
        with allure.step('Отправить запрос на удаление пользователя'):
            response = requests.delete(f"{self.url}/user/{username}")
        with allure.step('Проверить ответ по схеме после удаления пользователя'):
            validate(instance=response.json(), schema=schema)
        logger.info_logging(response)
        allure_attach.info_attaching(response)
        return response
