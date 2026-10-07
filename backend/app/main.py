from fastapi import FastAPI 
from app.routes import chat
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="AI Portfolio Assistant", version="1.0.0")
app.include_router(chat.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        os.getenv("FRONTEND_URL", "")
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)