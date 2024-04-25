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

    @allure.step("Создание пользователя")
    def create_users(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.header.basic,
            json=self.payload.create_user
        )
        assert response.status_code == 200, response.json()
        #Добавляем ответ к отчету
        self.attach_response(response.json())
        # Валидация ответа по модели
        model = UserModel(**response.json())
        return  model


    @allure.step("Получение информации о юзере")
    def get_user_id(self,uuid):
        response = requests.get(
            url=self.endpoints.get_user_id(uuid),
            headers=self.header.basic
        )
        # Добавляем ответ к отчету
        self.attach_response(response.json())
        # Валидация ответа по модели
        model = UserModel(**response.json())
        return model

        