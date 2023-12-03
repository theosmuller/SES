from typing import List
from model.Course import Course

class CourseService:
    def __init__(self):
            # In a real app, this might interact with a database
            self.courses = []

    def get_course_by_name(self, course_name: str) -> Course:
        for course in self.courses:
            if course.name == course_name:
                return course
            return None
