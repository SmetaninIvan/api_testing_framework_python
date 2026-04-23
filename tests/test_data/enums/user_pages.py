from enum import Enum


class UserPages(Enum):
    FIRST_PAGE = "users?page=1"
    SECOND_PAGE = "users?page=2"
    THIRD_PAGE = "users?page=3"