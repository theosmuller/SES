from fastapi import FastAPI
from .routes.course import router as course_router
from .routes.university import router as university_router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175"
]


def create_app()->FastAPI:
    app = FastAPI()
    app.include_router(course_router)
    app.include_router(university_router)
    app.add_middleware(
    CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )
    return app