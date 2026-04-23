from typing import Any, List, Dict


def get_user_first_names(obj_list: List[Dict[str, Any]]) -> list[str]:
    return [user['first_name'] for user in obj_list]


def compare_users(list1: List[str], list2: List[str]) -> bool:
    if len(list1) != len(list2):
        raise ValueError("Lists are not equal")
    return set(list1) == set(list2)
