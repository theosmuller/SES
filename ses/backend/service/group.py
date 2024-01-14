from ast import List
from ses.schemas.schemas import Group
from ses.core.repository import MongoRepo

class GroupService:
    def __init__(self):
        self.repo = MongoRepo(
            Group,
            "mongodb://localhost:27017",
            "ses"
        )

    def get_group_by_name(self, group_name: str) -> Group:
        return self.repo.get_by({"name": group_name})

    def add_group(self, group: Group):
        self.repo.add(group)

    def get_groups_by_remote(self, remote: bool) -> List(Group):
        return self.repo.get_by({"remote": remote})
