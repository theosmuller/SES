from ses_backend.api.setup_app import create_app
import uvicorn


# Define your API routes here
def main():
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()