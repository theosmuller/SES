from pydantic import BaseModel, Field, validator
from uuid import uuid4
from enum import StrEnum
from typing import Any

class Entity(BaseModel):
    id: str = Field(default_factory=lambda : str(uuid4()).replace("-", ""), alias="_id" )

class Admin(Entity):
    name: str
    email: str
    university_id: str

class Program(Entity):
    university_id: str
    name: str

class Course(Entity):
    university_id: str
    program_ids: list[str]
    name: str
    credits: int
    pre_requisites: list[str] = Field(default_factory=list)

class University(Entity):
    name: str

class Campus(Entity):
    university_id: str
    name: str
    address: str


class Professor(Entity):
    name: str
    email: str
    university_id: str

class Section(Entity):
    course_id: str
    section_name: str
    professor_id: str
    campus: str
    building: str
    room: str
    online: bool
    timeslots: list[str] = Field(default_factory=list)

class Student(Entity):
    name: str
    email: str
    program_id: str
    university_id: str
    completed_courses: list[str] = Field(default_factory=list)

class Enrollment(Entity):
    student_id: str
    course_id: str
    year: int
    section_id: str
    semester: int

    @validator("semester")
    def semester_must_be_positive(cls, v:int, **kwargs:Any)->int:
        if v <= 0:
            raise ValueError('semester must be positive')
        return v
    
    @validator("year")
    def year_must_be_positive(cls, v:int, **kwargs:Any)->int:
        if v <= 0:
            raise ValueError('year must be positive')
        return v


class DayOfWeek(StrEnum):
    M = 'Monday'
    T = 'Tuesday'
    W = 'Wednesday'
    Th = 'Thursday'
    F = 'Friday'
    S = 'Saturday'


class TimeSlot(Entity):
    university_id: str
    day: DayOfWeek
    start_time: float
    end_time: float

    @validator("end_time")
    def end_time_must_be_greater_than_start_time(cls, v:float, values:dict[str, Any], **kwargs:Any)->float:
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError('end_time must be greater than start_time')
        return v

class OptimizerSection(Entity):
    timeslots: list[TimeSlot]
    section_id: str

class TableMetaData(Entity):
    university_id: str
    timeslots: list[str]

class TimeTable(Entity):
    year: int
    semester: int
    university_id: str
    student_id: str
    timeslots: list[TimeSlot]

    @validator("timeslots")
    def timeslots_must_not_overlap(cls, v:list[TimeSlot], values:dict[str, Any], **kwargs:Any)->list[TimeSlot]:
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                if v[i].day == v[j].day and v[i].start_time < v[j].end_time and v[i].end_time > v[j].start_time:
                    raise ValueError('timeslots must not overlap')
        return v
