import allure
import pytest
from src.models.user_models import UserModel, UserListResponseModel


class TestApiUsers:

    @allure.feature("User List Operations")
    @allure.title("Test case: User list validation")
    @pytest.mark.parametrize('page', [1, 2])
    def test_get_users(self, user_client, page):
        with allure.step(f"Get response object of users for page {page}"):
            user_response = user_client.get_users(page)

        with allure.step("Check status code"):
            assert user_response.status_code == 200, "Status-code not equal 200"

        with allure.step("Get validation data"):
            model = UserListResponseModel(**user_response.json())

        with allure.step("Check validation"):
            assert model.page == page
            assert len(model.data) > 0
            assert len(model.data) == model.per_page

    @allure.feature("Single User Operations")
    @allure.title("Test case: Single user validation")
    @pytest.mark.parametrize('user_id', range(1, 7))
    def test_get_single_user(self, user_client, user_id):
        with allure.step(f"Get response object for user_id {user_id}"):
            single_user_response = user_client.get_user(user_id)

        with allure.step("Check status code"):
            assert single_user_response.status_code == 200, "Status-code not equal 200"

        with allure.step("Get validation data"):
            user_model_data = UserModel(**single_user_response.json()['data'])

        with allure.step("Check validation"):
            assert user_model_data.email
            assert user_model_data.id == user_id
            assert user_model_data.first_name
            assert user_model_data.last_name
            assert user_model_data.avatar
