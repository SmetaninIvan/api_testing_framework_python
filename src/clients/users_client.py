from .base_client import BaseClient


class UserClient(BaseClient):

    def get_users(self, page=1):
        return self.get("/users", params=f"page={page}")

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")
