import requests
from src.helpers.user_helper import *
from .test_data.expected_users_info import USER_LIST_EXPECTED_NAMES
from .test_data.enums.user_pages import UserPages

HEADERS = {"x-api-key": "reqres_6684f794f8a543f2abeb1451b0417feb"}
BASE_URL = "https://reqres.in/api"


class TestApiUsers:

    def test_get_users(self):
        user_response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)

        assert user_response.status_code == 200, "Status-code not equal 200"

        data_body = user_response.json()
        assert 'data' in data_body
        assert 'page' in data_body
        assert 'total' in data_body
        assert 'total_pages' in data_body

    def test_get_single_user(self):
        single_user_response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)

        assert single_user_response.status_code == 200, "Status-code not equal 200"
        single_user_data = single_user_response.json()['data']

        assert isinstance(single_user_data['id'], int)
        assert isinstance(single_user_data['first_name'], str)
        assert isinstance(single_user_data['last_name'], str)

        assert '@' in single_user_data['email']
        assert ".jpg" in single_user_data['avatar'][-4:]

    def test_get_users_list(self):
        """Тест сравнивает список имен с сервера и из тестовых данных"""

        user_response = requests.get(f"{BASE_URL}/{UserPages.SECOND_PAGE.value}", headers=HEADERS)

        assert user_response.status_code == 200, "Status-code not equal 200"

        user_list_response = get_user_first_names(user_response.json()['data'])

        assert compare_users(user_list_response, USER_LIST_EXPECTED_NAMES["page_2"])

