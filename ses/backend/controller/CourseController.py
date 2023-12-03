from typing import Union
from fastapi import APIRouter, HTTPException
from service.CourseService import CourseService
from model.Course import Course

router = APIRouter()
courseService = CourseService()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/courses/{course_id}")
def get_course(course_id: int, q: Union[str, None] = None):
    return {"course_id": course_id, "q": q}

@ router.get("/courses/{course_name}")
def get_course(course_name: Union[str,None] = None):
    return courseService.search_course_by_name(course_name)

@router.put("/courses/{course_id}")
def add_course(course_id: int, course: Course):
    return {"course_name": course.name, "course_id": course_id}
