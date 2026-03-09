from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router

app = FastAPI(title="College AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev ke liye ok
    allow_credentials=True,
    allow_methods=["*"],   # OPTIONS, POST, etc
    allow_headers=["*"],
)

app.include_router(chat_router)