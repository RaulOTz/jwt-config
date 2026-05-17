from fastapi import FastAPI

from app.api.auth import router as auth_router

from app.core.database import (
    engine, 
    Base
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "JWT Auth API running"
    }