import uvicorn

def main():
    uvicorn.run(
        app = "ses.backend.api:create_app",
        host = "0.0.0.0",
        port = 8000,
    )
    

if __name__ == "__main__":
    main()