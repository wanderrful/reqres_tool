from dataclasses import dataclass
from typing import List

from reqres_tool.src.models.user import User


@dataclass
class ListUsersResponse:
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
    ad: dict

    def __post_init__(self):
        # Since "data" is a List of User classes, we need to parse the list appropriately!
        users = []
        for user in self.data:
            users.append(User(**user))
        self.data = users
