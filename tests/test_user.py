from api.user import UserApiMethods
from helpers.helpers import load_json
from schemas.user_schemas import created_user, get_user, deleted_user, updated_user, get_not_existing_user


class TestUserPositive:

    def test_create_user(self, api_url):
        request_body = load_json("user1.json")
        response = UserApiMethods(url=api_url).create_user(body=request_body, schema=created_user)
        body = response.json()
        assert response.status_code == 200
        assert body["message"] == '1223334444'
        username = request_body["username"]
        UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)


    def test_get_existing_user(self, api_url, pre_created_user, delete_pre_created_user):
        username = pre_created_user["username"]
        response = UserApiMethods(url=api_url).get_user_by_username(username, schema=get_user)
        body = response.json()
        assert response.status_code == 200
        assert body["id"] == int(pre_created_user["id"])

    def test_delete_existing_user(self, api_url, pre_created_user):
        username = pre_created_user["username"]
        response = UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)
        body = response.json()
        assert response.status_code == 200
        assert body["message"] == username

    def test_update_existing_user(self, api_url, pre_created_user, delete_pre_created_user):
        username = pre_created_user["username"]
        request_body = load_json("user1_changed.json")
        response_put = UserApiMethods(url=api_url).update_user_by_username(username, request_body, schema=updated_user)
        body_put = response_put.json()
        response_get = UserApiMethods(url=api_url).get_user_by_username(username, schema=get_user)
        body_get = response_get.json()
        assert response_put.status_code == 200
        assert body_put["message"] == str(request_body["id"])
        assert body_get["id"] == request_body["id"] == pre_created_user["id"]
        assert body_get["username"] == request_body["username"] == username
        assert body_get["firstName"] == request_body["firstName"]
        assert body_get["lastName"] == request_body["lastName"]
        assert body_get["email"] == request_body["email"]
        assert body_get["password"] == request_body["password"]

class TestUserNegative:
    def test_get_non_existing_user(self, api_url, pre_created_user):
        username = pre_created_user["username"]
        UserApiMethods(url=api_url).delete_user_by_username(username, schema=deleted_user)
        response = UserApiMethods(url=api_url).get_user_by_username(username, schema=get_not_existing_user)
        body = response.json()
        assert response.status_code == 404
        assert body["message"] == "User not found"




