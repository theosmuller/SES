from typing import Optional
from fastapi import APIRouter
from ..service.course import CourseService
from ses.schemas.schemas import Course

router = APIRouter()
courseService = CourseService()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/courses/{course_name}")
def get_course_by_name(course_name: str):
    return courseService.get_course_by_name(course_name)
    
@router.post("/courses")
def add_course(course: Course):
    return courseService.add_course(course)
