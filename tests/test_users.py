import allure
import pytest
from config.base_test import BaseTest


@allure.epic("CREATE")
@allure.feature("Users")
class TestUsers(BaseTest):
    @pytest.mark.crud
    @allure.title("Create New Users")
    def test_create_user(self):
        print("-----START_TEST:CREATE_USER-----")
        print("CREATE_USER:")
        self.api_users.create_users()
        print("THE_TEST_IS_COMPLETED")

    @pytest.mark.crud
    @allure.title("Get User")
    def test_get_user(self):
        print("-----START_TEST:GET_USER-----")
        user = self.api_users.create_users()
        print("CREATE_USER:")
        print("GET_USER:")
        self.api_users.get_user_id(user.uuid)
        print("THE_TEST_IS_COMPLETED")

    @pytest.mark.crud
    @allure.title("Update User")
    def test_update_user(self):
        print("-----START_TEST:UPDATE_USER-----")
        print("CREATE_USER")
        user = self.api_users.create_users()
        print("GET_USER")
        before_get=self.api_users.get_user_id(user.uuid)
        print("UPDATE_USER")
        self.api_users.update_user(user.uuid)
        print("GET_AFTER_THE_UPDATE")
        after_get=self.api_users.get_user_id(user.uuid)
        assert before_get != after_get, "Error update user"
        print("THE_TEST_IS_COMPLETED")

    @pytest.mark.crud
    @allure.title("Delete User")
    def test_delete_user(self):
        print("-----START_TEST:DELETE_USER-----")
        print("CREATE_USER")
        user = self.api_users.create_users()
        print("GET_USER")
        before_get = self.api_users.get_user_id(user.uuid)
        print("DELETE_USER")
        self.api_users.delete_user(user.uuid)
        print("GET_AFTER_THE_DELETE")
        after_get = self.api_users.get_user_id(user.uuid)




