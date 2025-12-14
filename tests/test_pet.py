from api.pet import PetApiMethods
from helpers.json_helper import load_json
from schemas.pet_schemas import created_pet, deleted_pet, get_pet, updated_pet, get_not_existing_pet


class TestPetPositive:

    def test_create_pet(self, api_url):
        request_body = load_json("pet.json")
        response = PetApiMethods(url=api_url).create_pet(body=request_body, schema=created_pet)
        body = response.json()
        assert response.status_code == 200
        assert body["id"] == request_body["id"]
        assert body["category"] == request_body["category"]
        assert body["category"]["name"] == request_body["category"]["name"]
        assert body["name"] == request_body["name"]
        PetApiMethods(url=api_url).delete_pet_by_id(body["id"], schema=deleted_pet)

    def test_get_existing_pet(self, api_url, create_default_pet, delete_default_pet):
        pet_id = create_default_pet["id"]
        response = PetApiMethods(url=api_url).get_pet_by_id(pet_id, schema=get_pet)
        body = response.json()
        assert response.status_code == 200
        assert body["id"] == pet_id
        assert body["category"]["name"] == create_default_pet["category"]["name"]
        assert body["name"] == create_default_pet["name"]

    def test_update_pet(self, api_url, create_default_pet, delete_default_pet):
        request_body = load_json("default_pet_changed.json")
        response_put = PetApiMethods(url=api_url).update_pet(body=request_body, schema=updated_pet)
        body_put = response_put.json()
        pet_id = create_default_pet["id"]
        response_get = PetApiMethods(url=api_url).get_pet_by_id(pet_id, schema=get_pet)
        body_get = response_get.json()
        assert response_put.status_code == 200
        assert body_put["id"] == request_body["id"] == create_default_pet["id"]
        assert body_get["name"] == request_body["name"]
        assert body_get["category"]["name"] == request_body["category"]["name"]
        assert body_get["tags"][0]["name"] == request_body["tags"][0]["name"]
        assert body_get["status"] == request_body["status"]

    def test_delete_existing_pet(self, api_url, create_default_pet):
        pet_id = create_default_pet["id"]
        response = PetApiMethods(url=api_url).delete_pet_by_id(pet_id, schema=deleted_pet)
        body = response.json()
        assert response.status_code == 200
        assert body["message"] == str(pet_id)

class TestPetNegative:
    def test_get_not_existing_pet(self, api_url, create_default_pet):
        pet_id = create_default_pet["id"]
        PetApiMethods(url=api_url).delete_pet_by_id(pet_id, schema=deleted_pet)
        response = PetApiMethods(url=api_url).get_pet_by_id(pet_id, schema=get_not_existing_pet)
        body = response.json()
        assert response.status_code == 404
        assert body["message"] == "Pet not found"
