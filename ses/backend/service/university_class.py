from ses.schemas.schemas import UniversityClass
from ses.core.repository import MongoRepo

class UniversityClassService:
    def __init__(self):
        self.repo = MongoRepo(
            UniversityClass,
            "mongodb://localhost:27017",
            "ses"
        )

    def get_class_by_name(self, class_name: str) -> UniversityClass:
        return self.repo.get_by({"name": class_name})

    def add_class(self, university_class: UniversityClass):
        self.repo.add(university_class)