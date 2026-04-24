from pydantic import BaseModel, EmailStr
from typing import List

class UserModel(BaseModel):

    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str
    # data: List[User]