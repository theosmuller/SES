from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    name: str
    attendants: int
    average_grade: float
    is_available: Optional[bool] = None
