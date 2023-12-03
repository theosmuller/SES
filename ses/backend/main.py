from fastapi import FastAPI
from controller import CourseController

app = FastAPI()

app.include_router(CourseController.router, tags=["courses"])
