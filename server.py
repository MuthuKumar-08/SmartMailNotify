from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "SmartMailNotify",
        "status": "Running",
        "message": "Server is ready 🚀"
    }

@app.post("/gmail/webhook")
async def gmail_webhook(request: Request):
    body = await request.json()

    print("=" * 60)
    print("📩 Gmail Push Notification Received")
    print(body)
    print("=" * 60)

    return {"status": "received"}