import pytest
from src.data_prodject.config import BASE_URL, HEADERS
from src.clients.users_client import UserClient


@pytest.fixture
def user_client():
    return UserClient(BASE_URL, HEADERS)
