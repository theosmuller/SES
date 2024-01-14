from ses.schemas.schemas import University
from ses.core.repository import MongoRepo

class UniversityService:
    def __init__(self):
        self.repo = MongoRepo(
            University,
            "mongodb://localhost:27017",
            "ses"
        )

    def get_university_by_name(self, university_name: str) -> University:
        return self.repo.get_by({"name": university_name})

    def add_university(self, university: University):
        self.repo.add(university)