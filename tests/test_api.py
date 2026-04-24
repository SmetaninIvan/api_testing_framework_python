import pytest
from src.helpers.user_helper import *
from .test_data.expected_users_info import USER_LIST_EXPECTED_NAMES
from src.models.user_models import UserModel

class TestApiUsers:

    @pytest.mark.parametrize('page', [1, 2, 3])
    def test_get_users(self, user_client, page):

        user_response = user_client.get_users(page)

        assert user_response.status_code == 200, "Status-code not equal 200"

        data_body = user_response.json()
        assert 'data' in data_body
        assert 'page' in data_body
        assert 'total' in data_body
        assert 'total_pages' in data_body

        user_list_response = get_user_first_names(user_response.json()['data'], "first_name")

        assert compare_users(user_list_response, USER_LIST_EXPECTED_NAMES[f"page_{page}"])

    @pytest.mark.parametrize('user_id', range(1, 7))
    def test_get_single_user(self, user_client, user_id):
        single_user_response = user_client.get_user(user_id)

        assert single_user_response.status_code == 200, "Status-code not equal 200"
        # single_user_data = single_user_response.json()['data']

        model = UserModel(**single_user_response.json())

        assert model.data.id == user_id
        # assert isinstance(single_user_data['first_name'], str)
        # assert isinstance(single_user_data['last_name'], str)
        #
        # assert '@' in single_user_data['email']
        # assert ".jpg" in single_user_data['avatar'][-4:]
