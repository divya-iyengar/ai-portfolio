from fastapi import FastAPI 
from app.routes import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Portfolio Assistant", version="1.0.0")
app.include_router(chat.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)