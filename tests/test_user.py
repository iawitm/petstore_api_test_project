import allure

from api.user import UserApiMethods
from helpers.json_helper import load_json
from schemas.user_schemas import created_user, get_user, deleted_user, updated_user, get_not_existing_user


@allure.epic('Проверка методов для пользователя')
@allure.feature("Проверка позитивных кейсов для методов пользователя")
class TestUserPositive:

    @allure.title("Создание пользователя")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_create_user(self, api_url):
        request_body = load_json("user.json")
        response = UserApiMethods(url=api_url).create_user(body=request_body, schema=created_user)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response.status_code == 200
        with allure.step('Проверить, что в ответе приходит id созданного пользователя'):
            assert body["message"] == str(request_body["id"])
        username = request_body["username"]
        UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)

    @allure.title("Получение существующего пользователя")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_get_existing_user(self, api_url, create_default_user, delete_default_user):
        username = create_default_user["username"]
        response = UserApiMethods(url=api_url).get_user_by_username(username, schema=get_user)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response.status_code == 200
        with allure.step('Проверить, что в ответе приходит id запрашиваемого пользователя'):
            assert body["id"] == create_default_user["id"]

    @allure.title("Обновление существующего пользователя")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_update_existing_user(self, api_url, create_default_user, delete_default_user):
        username = create_default_user["username"]
        request_body = load_json("default_user_changed.json")
        response_put = UserApiMethods(url=api_url).update_user_by_username(username, request_body, schema=updated_user)
        body_put = response_put.json()
        response_get = UserApiMethods(url=api_url).get_user_by_username(username, schema=get_user)
        body_get = response_get.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response_put.status_code == 200
        with allure.step('Проверить, что в ответе на обновление приходит id обновленного пользователя'):
            assert body_put["message"] == str(request_body["id"])
        with allure.step('Проверить, что в ответе на получение приходит id обновленного пользователя '
                         'и оно равно изначальному'):
            assert body_get["id"] == request_body["id"] == create_default_user["id"]
        with allure.step('Проверить, что в ответе на получение приходит username обновленного пользователя '
                         'и он равен изначальному'):
            assert body_get["username"] == request_body["username"] == username
        with allure.step('Проверить, что в ответе на получение приходит измененное имя пользователя'):
            assert body_get["firstName"] == request_body["firstName"]
        with allure.step('Проверить, что в ответе на получение приходит измененная фамилия пользователя'):
            assert body_get["lastName"] == request_body["lastName"]
        with allure.step('Проверить, что в ответе на получение приходит измененный email пользователя'):
            assert body_get["email"] == request_body["email"]

    @allure.title("Удаление существующего пользователя")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_delete_existing_user(self, api_url, create_default_user):
        username = create_default_user["username"]
        response = UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 200'):
            assert response.status_code == 200
        with allure.step('Проверить, что при удалении в ответе приходит username пользователя'):
            assert body["message"] == username


@allure.epic('Проверка методов для пользователя')
@allure.feature("Проверка негативных кейсов для методов пользователя")
class TestUserNegative:

    @allure.title("Получение несуществующего пользователя")
    @allure.tag('Регресс', 'API', 'Normal')
    @allure.label('API')
    @allure.severity('Normal')
    def test_get_non_existing_user(self, api_url, create_default_user):
        username = create_default_user["username"]
        UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)
        response = UserApiMethods(url=api_url).get_user_by_username(username, schema=get_not_existing_user)
        body = response.json()
        with allure.step('Проверить, что значение статус-кода равно 404'):
            assert response.status_code == 404
        with allure.step('Проверить, что в ответе приходит сообщение "User not found"'):
            assert body["message"] == "User not found"
