from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Course(BaseModel):
    pass


class University(BaseModel):
    name: str
    courses: list[Course]


class Professor(BaseModel):
    username: str


class Student(BaseModel):
    semester: int
    registration_number: str


Role = Professor | Student


class UserProfile(BaseModel):
    email: str
    course: str
    password: str  # Hashed
    role: Role


class UniversityClass(BaseModel):
    name: str
    students: list[Student]
    course: Course
    offered_to: list[Course]
    requirements: list["UniversityClass"]
    semester: int


class Group(BaseModel):
    name: str
    max_students: int
    professor: Professor
    remote: bool


class Location(BaseModel):
    campus: str
    building: str
    room: str

class Day(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    content: list[str]


class TimeAllotment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    days: list[Day]