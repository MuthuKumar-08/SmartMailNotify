from fastapi import FastAPI

from gmail.auth import authenticate
from gmail.service import process_emails
from database.db import create_database

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "SmartMailNotify",
        "status": "Running",
        "message": "Server is ready 🚀"
    }


@app.post("/check-emails")
def check_emails():

    print("\n🚀 SmartMailNotify Triggered\n")

    create_database()

    creds = authenticate()

    process_emails(creds)

    return {
        "status": "success",
        "message": "Emails processed successfully"
    }