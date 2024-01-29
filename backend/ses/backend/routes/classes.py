from fastapi import APIRouter, HTTPException

router = APIRouter()

# Simulate a database with a dictionary
classes = {
    1: {"name": "Compilers", "code": "INF003", "credits": 3, "year": 2024, "sections": [
        {"section": "001", "id": 1, "professor": "Dr. Smith", "time": [
            {"day": "Monday", "start_time": "10:00", "end_time": "11:00"},
            {"day": "Wednesday", "start_time": "10:00", "end_time": "11:00"}
        ], "location": "Building 1, Room 101"},
        {"section": "002", "id": 2, "professor": "Dr. Lloyd", "time": [
            {"day": "Monday", "start_time": "11:00", "end_time": "12:00"},
            {"day": "Wednesday", "start_time": "11:00", "end_time": "12:00"}
        ], "location": "Building 1, Room 101"}
    ]},
    2: {"name": "Operating Systems", "code":"INF004", "credits": 5, "year": 2024, "sections": [
        {"section": "001", "id": 1, "professor": "Dr. Keen", "time": [
            {"day": "Monday", "start_time": "10:00", "end_time": "11:00"},
            {"day": "Wednesday", "start_time": "10:00", "end_time": "11:00"}
        ], "location": "Building 1, Room 101"},
        {"section": "002", "id": 2, "professor": "Dr. Bay", "time": [
            {"day": "Monday", "start_time": "14:00", "end_time": "15:00"},
            {"day": "Wednesday", "start_time": "11:00", "end_time": "12:00"}
        ], "location": "Building 1, Room 101"}
    ]},
    3: {"name": "Data Structures", "code":"INF005", "credits": 3, "year": 2024, "sections": [
        {"section": "001", "id": 1, "professor": "Dr. Smith", "time": [
            {"day": "Monday", "start_time": "10:00", "end_time": "11:00"},
            {"day": "Wednesday", "start_time": "10:00", "end_time": "11:00"}
        ], "location": "Building 1, Room 102"},
        {"section": "002", "id": 2, "professor": "Dr. Lloyd", "time": [
            {"day": "Monday", "start_time": "11:00", "end_time": "12:00"},
            {"day": "Wednesday", "start_time": "11:00", "end_time": "12:00"}
        ], "location": "Building 1, Room 102"}
    ]},
}

@router.get("/class/{id}")
async def get_class(id: int):
    if id in classes:
        return classes[id]
    else:
        raise HTTPException(status_code=404, detail="Class not found")