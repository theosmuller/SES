from fastapi import APIRouter, HTTPException, Response
from ses_backend.schemas.schemas import Professor, Course
from ses_backend.core.persistance import MongoDBRepository


router = APIRouter()
repo_professor = MongoDBRepository(Professor)
repo_course = MongoDBRepository(Course)

@router.get("/university/{university_id}/professor")
def get_professors(university_id: str)->list[Professor]:
    query = {"university_id": str(university_id)}
    r = repo_professor.find_by(query)
    return r

@router.get("/university/{university_id}/professor/{professor_id}")
def get_professor(university_id: str, professor_id: str)->Professor:
    query = {"university_id": str(university_id), "_id": str(professor_id)}
    r = repo_professor.find_by(query)
    if not r:
        raise HTTPException(status_code=404, detail="Professor not found")
    return r[0]

@router.post("/university/{university_id}/professor")
def create_professor(university_id: str, professor: Professor, response: Response):
    professor.university_id = str(university_id)
    repo_professor.create(professor)
    response.status_code = 202
    return {"message": "Professor created", "professor": professor}

@router.put("/university/{university_id}/professor/{professor_id}")
def update_professor(university_id: str, professor_id: str, professor: Professor, response: Response):
    professor.university_id = str(university_id)
    repo_professor.update(professor)
    response.status_code = 202
    return {"message": "Professor updated", "professor": professor}

@router.delete("/university/{university_id}/professor/{professor_id}")
def delete_professor(university_id: str, professor_id: str, response: Response):
    repo_professor.delete(str(professor_id))
    response.status_code = 204
    return {"message": "Professor deleted"}

@router.get("/university/{university_id}/professor/{professor_id}/courses")
def get_courses(university_id: str, professor_id: str)->list[Course]:
    query = {"professor_id": professor_id}
    r = repo_course.find_by(query)
    return r