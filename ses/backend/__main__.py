import uvicorn
from ses.backend.pymongo_get_database import get_database

def main():
    db = get_database()
    uvicorn.run(
        app = "ses.backend.api:create_app",
        host = "0.0.0.0",
        port = 8000,
    )
    

if __name__ == "__main__":
    main()