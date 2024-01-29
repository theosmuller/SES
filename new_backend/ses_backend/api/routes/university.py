from fastapi import APIRouter, Response
from ses_backend.schemas.schemas import University, TimeSlot
from ses_backend.core.persistance import MongoDBRepository

router = APIRouter()
repo_university = MongoDBRepository(University)
repo_timeslots = MongoDBRepository(TimeSlot)

@router.get("/university")
async def get_universities():
    return repo_university.get_all()

@router.get("/university/{university_id}")
async def get_university(university_id: str):
    return repo_university.get(str(university_id))

@router.post("/")
async def create_university(name: str, response: Response):
    uni = University(name=name)
    repo_university.create(uni)
    # return accepted
    response.status_code = 202
    return {"message": "University created", "university": uni}


@router.put("/university/{university_id}")
async def update_university(university_id: str, university: University, response: Response):
    repo_university.update(university)
    # return accepted
    response.status_code = 202
    return {"message": "University updated", "university": university}

@router.delete("/university/{university_id}")
async def delete_university(university_id: str, response: Response):
    # Your code here
    repo_university.delete(str(university_id))
    response.status_code = 204
    return {"message": "University deleted"}

@router.get("/university/{university_id}/timeslots")
def get_timeslots(university_id: str)->list[TimeSlot]:
    query = {"university_id": str(university_id)}
    r = repo_timeslots.find_by(query)
    return r

@router.post("/university/{university_id}/timeslots")
def create_timeslot(university_id: str, timeslot: TimeSlot, response: Response):
    timeslot.university_id = str(university_id)
    repo_timeslots.create(timeslot)
    response.status_code = 202
    return {"message": "TimeSlot created", "timeslot": timeslot}

@router.put("/university/{university_id}/timeslots/{timeslot_id}")
def update_timeslot(university_id: str, timeslot_id: str, timeslot: TimeSlot, response: Response):
    timeslot.university_id = str(university_id)
    repo_timeslots.update(timeslot)
    response.status_code = 202
    return {"message": "TimeSlot updated", "timeslot": timeslot}

@router.delete("/university/{university_id}/timeslots/{timeslot_id}")
def delete_timeslot(university_id: str, timeslot_id: str, response: Response):
    repo_timeslots.delete(str(timeslot_id))
    response.status_code = 204
    return {"message": "TimeSlot deleted"}



