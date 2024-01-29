from ses_backend.core.persistance import MongoDBRepository
from ses_backend.schemas.schemas import University, TimeSlot, DayOfWeek, Professor, Student, Program, Course
from pathlib import Path
from faker import Faker


def make_universities():
    assets = Path("~/backend/ses_backend/assets").expanduser()
    repo_university = MongoDBRepository(University)

    with open(assets / "world-universities.csv") as f:
        data = f.readlines()
        for line in data:
            line = line.split(",")
            uni = University(name=line[1])
            repo_university.create(uni)

def make_timeslots(university_id:str):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start_times = [8.5, 10.5, 13.5, 15.5, 17.5]
    end_times = [10, 12, 15, 17, 19]
    repo_timeslots = MongoDBRepository(TimeSlot)
    for day in days:
        for start, end in zip(start_times, end_times):
            timeslot = TimeSlot(university_id=university_id, day=DayOfWeek(day), start_time=start, end_time=end)
            repo_timeslots.create(timeslot)


def make_professors(university_id:str):
    repo_professor = MongoDBRepository(Professor)
    fake = Faker()
    professor = Professor(name=fake.name(), email=fake.email(), university_id=university_id)
    repo_professor.create(professor)

cool_programs = ["Computer Science", "Classics", "Mathematics", "Music"]

def make_programs(university_id:str, name: str):
    repo_program = MongoDBRepository(Program)
    program = Program(name=name, university_id=university_id)
    repo_program.create(program)

def make_students():
    repo_student = MongoDBRepository(Student)
    fake = Faker()
    student = Student(name=fake.name(), email=fake.email(), university_id="f75c7d6296c548978a0cbd53d2b295f0", program_id="28d9038f1d93422480ff2f8b72b2fa90")
    repo_student.create(student)

    
def make_course():
    repo_course = MongoDBRepository(Course)
    courses = []
    courses.append(Course(name="Introduction to Computer Science", university_id="f75c7d6296c548978a0cbd53d2b295f0", program_ids=["28d9038f1d93422480ff2f8b72b2fa90"], pre_requisites=[], credits=3))
    courses.append(Course(name="Introduction to Programming", university_id="f75c7d6296c548978a0cbd53d2b295f0", program_ids=["28d9038f1d93422480ff2f8b72b2fa90"], pre_requisites=[], credits=3))
    courses.append(Course(name="Introduction to Algorithms", university_id="f75c7d6296c548978a0cbd53d2b295f0", program_ids=["28d9038f1d93422480ff2f8b72b2fa90"], pre_requisites=[], credits=3))
    for course in courses:
        repo_course.create(course)

def make_course_w_prereq():
    repo_Course = MongoDBRepository(Course)
    course = Course(name="Advanced Algorithms", university_id="f75c7d6296c548978a0cbd53d2b295f0", program_ids=["28d9038f1d93422480ff2f8b72b2fa90"], pre_requisites=["adace7de3a20466ca5482cd531f74958"], credits=3)
    repo_Course.create(course)

cool_ids = {
    "MIT" : "f75c7d6296c548978a0cbd53d2b295f0",
    "CALTECH" : "ba6901ab28c94f47919c4f392f60e481",
    "Cambridge": "7ad7676565f346679270e30483219671",
    "Oxford" : "10aba2f87d014dd58af7217b6d29417b"
}
