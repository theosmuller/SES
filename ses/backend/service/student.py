from ses.schemas.schemas import Student
from ses.core.repository import MongoRepo

class StudentService:
    def __init__(self):
        self.repo = MongoRepo(
            Student,
            "mongodb://localhost:27017",
            "ses"
        )

    def get_student_by_registration_number(self, reg_number: str) -> Student:
        return self.repo.get_by({"registration_number": reg_number})

    def add_student(self, student: Student):
        self.repo.add(student)