from fastapi import APIRouter, HTTPException, Response
from ses_backend.schemas.schemas import Program, Course
from ses_backend.core.persistance import MongoDBRepository

router = APIRouter()
program_repo = MongoDBRepository(Program)
course_repo = MongoDBRepository(Course)

@router.get("/university/{university_id}/program")
def get_programs(university_id: str)->list[Program]:
    query = {"university_id": str(university_id)}
    r = program_repo.find_by(query)
    return r

@router.get("/university/{university_id}/program/{program_id}")
def get_program(university_id: str, program_id: str)->Program:
    query = {"university_id": str(university_id), "_id": str(program_id)}
    r = program_repo.find_by(query)
    if not r:
        raise HTTPException(status_code=404, detail="Program not found")
    return r[0]

@router.post("/university/{university_id}/program")
def create_program(university_id: str, program: Program, response: Response):
    program.university_id = str(university_id)
    program_repo.create(program)
    response.status_code = 202
    return {"message": "Program created", "program": program}

@router.put("/university/{university_id}/program/{program_id}")
def update_program(university_id: str, program_id: str, program: Program, response: Response):
    program.university_id = str(university_id)
    program_repo.update(program)
    response.status_code = 202
    return {"message": "Program updated", "program": program}

@router.delete("/university/{university_id}/program/{program_id}")
def delete_program(university_id: str, program_id: str, response: Response):
    program_repo.delete(str(program_id))
    response.status_code = 204
    return {"message": "Program deleted"}

@router.get("/university/{university_id}/program/{program_id}/courses")
def get_courses(university_id: str, program_id: str)->list[Course]:
    program = program_repo.get(program_id)
    query = {"program_ids": {"$in": [program.id]}}
    r = course_repo.find_by(query)
    return r