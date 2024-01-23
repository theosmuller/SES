from typing import Optional
from fastapi import APIRouter
from ..service.course import CourseService
from ..model.course import Course

router = APIRouter()
courseService = CourseService()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/courses/{course_id}")
def get_course(course_id: int, q: Optional[str] = None):
    return {"course_id": course_id, "q": q if q else 0}

@router.get("/courses/{course_name}")
def get_course_by_name(course_name: str):
    return courseService.get_course_by_name(course_name)
    
@router.put("/courses/{course_id}")
def add_course(course_id: int, course: Course):
    return {"course_name": course.name, "course_id": course_id}
