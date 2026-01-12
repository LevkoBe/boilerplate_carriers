from fastapi import FastAPI
from src.app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/health")
def health_check():
    return {"status": "ok", "project": settings.PROJECT_NAME}
