from fastapi import FastAPI
from src.app.core.config import settings
from src.app.api.v1.endpoints import carriers

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(carriers.router, prefix=f"{settings.API_V1_PREFIX}/carriers", tags=["carriers"])


@app.get("/health")
def health_check():
    return {"status": "ok", "project": settings.PROJECT_NAME}
