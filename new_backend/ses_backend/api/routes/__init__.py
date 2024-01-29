from ses_backend.api.routes.university import router as university_router
from ses_backend.api.routes.course import router as course_router
from ses_backend.api.routes.professor import router as professor_router
from ses_backend.api.routes.student import router as student_router
from ses_backend.api.routes.program import router as program_router


routers = [university_router, course_router, professor_router, student_router, program_router]