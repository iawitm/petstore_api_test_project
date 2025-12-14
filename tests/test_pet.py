import allure

from api.pet import PetApiMethods
from helpers.json_helper import load_json
from schemas.pet_schemas import created_pet, deleted_pet, get_pet, updated_pet, get_not_existing_pet


@allure.epic('Проверка методов для питомца')
@allure.feature("Проверка позитивных кейсов для методов питомца")
class TestPetPositive:

    @allure.title("Создание питомца")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_create_pet(self, api_url):
        request_body = load_json("pet.json")
        response = PetApiMethods(url=api_url).create_pet(body=request_body, schema=created_pet)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response.status_code == 200
        with allure.step('Проверить, что в ответе приходит id созданного питомца'):
            assert body["id"] == request_body["id"]
        with allure.step('Проверить, что в ответе приходит категория созданного питомца'):
            assert body["category"]["name"] == request_body["category"]["name"]
        with allure.step('Проверить, что в ответе приходит имя созданного питомца'):
            assert body["name"] == request_body["name"]
        PetApiMethods(url=api_url).delete_pet_by_id(body["id"], schema=deleted_pet)

    @allure.title("Получение существующего питомца")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_get_existing_pet(self, api_url, create_default_pet, delete_default_pet):
        pet_id = create_default_pet["id"]
        response = PetApiMethods(url=api_url).get_pet_by_id(pet_id, schema=get_pet)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response.status_code == 200
        with allure.step('Проверить, что в ответе приходит id запрашиваемого питомца'):
            assert body["id"] == pet_id
        with allure.step('Проверить, что в ответе приходит категория запрашиваемого питомца'):
            assert body["category"]["name"] == create_default_pet["category"]["name"]
        with allure.step('Проверить, что в ответе приходит имя запрашиваемого питомца'):
            assert body["name"] == create_default_pet["name"]

    @allure.title("Обновление питомца")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_update_pet(self, api_url, create_default_pet, delete_default_pet):
        request_body = load_json("default_pet_changed.json")
        response_put = PetApiMethods(url=api_url).update_pet(body=request_body, schema=updated_pet)
        body_put = response_put.json()
        pet_id = create_default_pet["id"]
        response_get = PetApiMethods(url=api_url).get_pet_by_id(pet_id, schema=get_pet)
        body_get = response_get.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response_put.status_code == 200
        with allure.step('Проверить, что в ответе на обновление приходит id обновленного питомца '
                         'и он равен изначальному'):
            assert body_put["id"] == request_body["id"] == create_default_pet["id"]
        with allure.step('Проверить, что в ответе на получение приходит измененное имя питомца'):
            assert body_get["name"] == request_body["name"]
        with allure.step('Проверить, что в ответе на получение приходит измененная категория питомца'):
            assert body_get["category"]["name"] == request_body["category"]["name"]
        with allure.step('Проверить, что в ответе на получение приходит измененный тег питомца'):
            assert body_get["tags"][0]["name"] == request_body["tags"][0]["name"]
        with allure.step('Проверить, что в ответе на получение приходит измененный статус питомца'):
            assert body_get["status"] == request_body["status"]

    @allure.title("Удаление существующего питомца")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_delete_existing_pet(self, api_url, create_default_pet):
        pet_id = create_default_pet["id"]
        response = PetApiMethods(url=api_url).delete_pet_by_id(pet_id, schema=deleted_pet)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response.status_code == 200
        with allure.step('Проверить, что при удалении в ответе приходит id питомца'):
            assert body["message"] == str(pet_id)


@allure.epic('Проверка методов для питомца')
@allure.feature("Проверка негативных кейсов для методов питомца")
class TestPetNegative:

    @allure.title("Получение несуществующего питомца")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_get_not_existing_pet(self, api_url, create_default_pet):
        pet_id = create_default_pet["id"]
        PetApiMethods(url=api_url).delete_pet_by_id(pet_id, schema=deleted_pet)
        response = PetApiMethods(url=api_url).get_pet_by_id(pet_id, schema=get_not_existing_pet)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 404'):
            assert response.status_code == 404
        with allure.step('Проверить, что в ответе приходит сообщение "Pet not found"'):
            assert body["message"] == "Pet not found"
