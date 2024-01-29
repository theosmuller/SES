from fastapi import APIRouter, HTTPException, Response
from ses_backend.schemas.schemas import Student, Program, Course, Enrollment, TimeTable
from ses_backend.core.persistance import MongoDBRepository



router = APIRouter()
repo_student = MongoDBRepository(Student)
repo_program = MongoDBRepository(Program)
repo_course = MongoDBRepository(Course)
repo_enrollment = MongoDBRepository(Enrollment)
repo_timetable = MongoDBRepository(TimeTable)

@router.get("/university/{university_id}/student")
def get_students(university_id: str)->list[Student]:
    query = {"university_id": str(university_id)}
    r = repo_student.find_by(query)
    return r

@router.get("/university/{university_id}/student/{student_id}")
def get_student(university_id: str, student_id: str)->Student:
    query = {"university_id": str(university_id), "_id": str(student_id)}
    r = repo_student.find_by(query)
    if not r:
        raise HTTPException(status_code=404, detail="Student not found")
    return r[0]

@router.post("/university/{university_id}/student")
def create_student(university_id: str, student: Student, response: Response):
    student.university_id = str(university_id)
    repo_student.create(student)
    response.status_code = 202
    return {"message": "Student created", "student": student}

@router.put("/university/{university_id}/student/{student_id}")
def update_student(university_id: str, student_id: str, student: Student, response: Response):
    student.university_id = str(university_id)
    repo_student.update(student)
    response.status_code = 202
    return {"message": "Student updated", "student": student}

@router.delete("/university/{university_id}/student/{student_id}")
def delete_student(university_id: str, student_id: str, response: Response):
    repo_student.delete(str(student_id))
    response.status_code = 204
    return {"message": "Student deleted"}

@router.get("/university/{university_id}/student/{student_id}/available")
def get_available_courses(university_id: str, student_id: str)->list[Course]:
    student = repo_student.get(student_id)
    pipeline = [
    {
        "$match": {
            "program_ids": student.program_id,
            "_id": {"$nin": student.completed_courses}
        }
    },
    {
        "$match": {
            "requirements": {
                "$not": {
                    "$elemMatch": {"$nin": student.completed_courses}
                }
            }
        }
    }
    ]
    r = repo_course.aggregate(pipeline)
    return r

@router.get("/university/{university_id}/student/{student_id}/enrollment")
def get_enrollments(university_id: str, student_id: str)->list[Enrollment]:
    query = {"student_id": str(student_id)}
    r = repo_enrollment.find_by(query)
    return r

@router.post("/university/{university_id}/student/{student_id}/enrollment")
def create_enrollment(university_id: str, student_id: str, enrollment: Enrollment, response: Response):
    enrollment.student_id = str(student_id)
    repo_enrollment.create(enrollment)
    response.status_code = 202
    return {"message": "Enrollment created", "enrollment": enrollment}

@router.get("/university/{university_id}/student/{student_id}/enrollment/timetable")
def get_timetable(university_id: str, student_id: str, year: int, semester: int)->list[Enrollment]:
    query = {"student_id": str(student_id), "year": year, "semester": semester}
    r = repo_enrollment.find_by(query)
    return r

@router.post("/university/{university_id}/student/{student_id}/enrollment/timetable")
def create_timetable(university_id: str, student_id: str, timetable: TimeTable, response: Response):
    timetable.student_id = str(student_id)
    repo_timetable.create(timetable)
    response.status_code = 202
    return {"message": "Timetable created", "timetable": timetable}

@router.put("/university/{university_id}/student/{student_id}/enrollment/timetable")
def update_timetable(university_id: str, student_id: str, timetable: TimeTable, response: Response):
    timetable.student_id = str(student_id)
    repo_timetable.update(timetable)
    response.status_code = 202
    return {"message": "Timetable updated", "timetable": timetable}