import allure
import pytest
from config.base_test import BaseTest


@allure.epic("CREATE")
@allure.feature("Users")
class TestUsers(BaseTest):

    # Тест на создание юзера
    @pytest.mark.regression
    @allure.title("Create New Users")
    def test_create_user(self):
        user = self.api_users.create_users()
        print("POST:")
        print(user)
        print("GET:")
        print(self.api_users.get_user_id(user.uuid))