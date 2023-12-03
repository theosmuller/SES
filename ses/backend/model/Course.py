from typing import Union
from pydantic import BaseModel

class Course(BaseModel):
    name: str
    attendants: int
    average_grade: float
    is_available: Union[bool, None] = None
