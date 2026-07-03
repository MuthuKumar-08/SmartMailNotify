from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "SmartMailNotify",
        "status": "Running",
        "message": "Server is ready 🚀"
    }