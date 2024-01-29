from fastapi import APIRouter, HTTPException, Response
from ses_backend.schemas.schemas import Course, Section
from ses_backend.core.persistance import MongoDBRepository

router = APIRouter()
course_repo = MongoDBRepository(Course)
section_repo = MongoDBRepository(Section)

@router.get("/university/{university_id}/course")
def get_courses(university_id: str)->list[Course]:
    query = {"university_id": str(university_id)}
    r = course_repo.find_by(query)
    return r

@router.get("/university/{university_id}/course/{course_id}")
def get_course(university_id: str, course_id: str)->Course:
    query = {"university_id": str(university_id), "_id": str(course_id)}
    r = course_repo.find_by(query)
    if not r:
        raise HTTPException(status_code=404, detail="Course not found")
    return r[0]

@router.post("/university/{university_id}/course")
def create_course(university_id: str, course: Course, response: Response):
    course.university_id = str(university_id)
    course_repo.create(course)
    response.status_code = 202
    return {"message": "Course created", "course": course}

@router.put("/university/{university_id}/course/{course_id}")
def update_course(university_id: str, course_id: str, course: Course, response: Response):
    course.university_id = str(university_id)
    course_repo.update(course)
    response.status_code = 202
    return {"message": "Course updated", "course": course}

@router.delete("/university/{university_id}/course/{course_id}")
def delete_course(university_id: str, course_id: str, response: Response):
    course_repo.delete(str(course_id))
    response.status_code = 204
    return {"message": "Course deleted"}

@router.get("/university/{university_id}/courses/{course_id}/{year}/section")
def get_sections(university_id: str, course_id: str, year: int)->list[Section]:
    query = {"university_id": str(university_id), "course_id": str(course_id), "year": year}
    r = section_repo.find_by(query)
    return r

@router.get("/university/{university_id}/courses/{course_id}/{year}/section/{section_id}")
def get_section(university_id: str, course_id: str, year: int, section_id: str)->Section:
    query = {"university_id": str(university_id), "course_id": str(course_id), "year": year, "_id": str(section_id)}
    r = section_repo.find_by(query)
    if not r:
        raise HTTPException(status_code=404, detail="Section not found")
    return r[0]

@router.post("/university/{university_id}/courses/{course_id}/{year}/section")
def create_section(university_id: str, course_id: str, year: int, section: Section, response: Response):
    section.university_id = str(university_id)
    section.course_id = str(course_id)
    section.year = year
    section_repo.create(section)
    response.status_code = 202
    return {"message": "Section created", "section": section}

@router.put("/university/{university_id}/courses/{course_id}/{year}/section/{section_id}")
def update_section(university_id: str, course_id: str, year: int, section_id: str, section: Section, response: Response):
    section.university_id = str(university_id)
    section.course_id = str(course_id)
    section.year = year
    section_repo.update(section)
    response.status_code = 202
    return {"message": "Section updated", "section": section}

@router.delete("/university/{university_id}/courses/{course_id}/{year}/section/{section_id}")
def delete_section(university_id: str, course_id: str, year: int, section_id: str, response: Response):
    section_repo.delete(str(section_id))
    response.status_code = 204
    return {"message": "Section deleted"}
