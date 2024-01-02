from pydantic import BaseModel, computed_field
from hashlib import sha256
from datetime import datetime
from typing import TypeVar

class Entity(BaseModel):         # MyPy thinks this is wrong but it is a bug!
    @computed_field(alias="_id") # type: ignore
    @property
    def id(self)->str:
        hash_id = sha256(datetime.now().isoformat().encode()).hexdigest()
        return str(hash_id)

EntityT = TypeVar("EntityT", bound=Entity)

class Course(Entity):
    pass


class University(Entity):
    name: str
    courses: list[Course]


class Professor(Entity):
    username: str


class Student(Entity):
    semester: int
    registration_number: str


Role = Professor | Student


class UserProfile(Entity):
    email: str
    course: str
    password: str  # Hashed
    role: Role


class UniversityClass(Entity):
    name: str
    students: list[Student]
    course: Course
    offered_to: list[Course]
    requirements: list["UniversityClass"]
    semester: int


class Group(Entity):
    name: str
    max_students: int
    professor: Professor
    remote: bool


class Location(Entity):
    campus: str
    building: str
    room: str
