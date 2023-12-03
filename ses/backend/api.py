from fastapi import FastAPI
from .routes.course import router as course_router


def create_app()->FastAPI:
    app = FastAPI()
    app.include_router(course_router)
    return app