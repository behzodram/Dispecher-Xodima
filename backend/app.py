from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI

from routes.token import router as token_router

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env.local")

app = FastAPI()

app.include_router(token_router)


@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Backend is running"
    }