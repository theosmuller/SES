from typing import Optional
from fastapi import APIRouter


router = APIRouter()
@router.get("/university/")
def send_universities():
    return [{"name": "University of Waterloo", "id": 1}, {"name": "University of Toronto", "id": 2}]
