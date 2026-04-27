from pydantic import BaseModel, EmailStr, field_validator, Field
from typing import List


class UserModel(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str = Field(pattern=r".*\.jpg$")


class UserListResponseModel(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserModel]
    # support: dict
    # _meta: dict
