import allure
import requests
from utils.helper import Helper
from services.users.models.payloads import Payloads
from services.users.models.endpoints import Endpoints
from services.users.models.user_model import UserModel
from config.headers import Headers


class UserAPI(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.header = Headers()
        self.payload = Payloads()

    @allure.step("CREATE_USER")
    def create_users(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.header.basic,
            json=self.payload.create_user
        )
        try:
            assert response.status_code == 200
            # Добавляем респонс к отчету
            self.attach_response(response.json())
            # Валидация респонс по модели
            model = UserModel(**response.json())
            return model
        except:
            print(str(response.status_code) + "- Error request")

    @allure.step("GET_USER")
    def get_user_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_id(uuid),
            headers=self.header.basic
        )
        if response.status_code == 200:
            self.attach_response(response.json())
            model = UserModel(**response.json())
            return model
        elif response.status_code == 404:
            print("User not found")
        else:
            print(response.status_code)

    @allure.step("UPDATE_USER")
    def update_user(self, uuid):
        response = requests.patch(
            url=self.endpoints.update_user(uuid),
            headers=self.header.basic,
            json=self.payload.update_user
        )
        try:
            assert response.status_code == 200, response.json()
            # Добавляем респонс к отчету
            self.attach_response(response.json())
            # Валидация респонс по модели
            model = UserModel(**response.json())
            return model
        except:
            print(str(response.status_code) + "Error request")


    @allure.step("DELETE_USER")
    def delete_user(self, uuid):
        response = requests.patch(
            url=self.endpoints.delete_user(uuid),
            headers=self.header.basic
        )
        try:
            assert response.status_code == 204, response.json()
            # Добавляем респонс к отчету
            self.attach_response(response.json())
            # Валидация респонс по модели
            model = UserModel(**response.json())
            return model
        except:
            print(str(response.status_code) + "- Error request")
