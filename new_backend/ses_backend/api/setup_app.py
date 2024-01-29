from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ses_backend.api.routes import routers


def create_app():
    app = FastAPI()
    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    for router in routers:
        app.include_router(router)
    
    return app
