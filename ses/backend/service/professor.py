from ses.schemas.schemas import Professor
from ses.core.repository import MongoRepo


class ProfessorService:
    def __init__(self):
        self.repo = MongoRepo(
            Professor,
            "mongodb://localhost:27017",
            "ses"
        )

    def get_professor_by_username(self, professor_username: str) -> Professor:
        return self.repo.get_by({"username": professor_username})

    def add_professor(self, professor: Professor):
        self.repo.add(professor)
