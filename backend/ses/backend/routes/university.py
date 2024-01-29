from typing import Optional
from fastapi import APIRouter


router = APIRouter()
@router.get("/university/")
def send_universities():
    return [{"name": "University of Waterloo", "id": 1}, {"name": "University of Toronto", "id": 2}]

@router.get("/university/{university_id}/timeslots")
def send_timeslots(university_id: int):
    return [{"id": 1, "start_time": "09:00", "end_time": "10:00"}, {"id": 2, "start_time": "10:00", "end_time": "11:00"}]