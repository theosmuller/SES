from ..model.course import Course
from ses.backend.pymongo_get_database import get_database
from ses.core.repository import MongoRepo

class CourseService:
    def __init__(self):
            self.courses = []
            self.repo = MongoRepo(
            Course,
            "mongodb://localhost:27017",
            "ses"
    )

    def get_course_by_name(self, course_name: str) -> Course:
        return self.repo.get_by([Course.name, course_name])
    
    def add_course(self, course: Course):
        self.repo.add(course)
    