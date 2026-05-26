from fastapi import APIRouter

from . import health, jobs, result, upload

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(upload.router, tags=["upload"])
api_router.include_router(jobs.router, tags=["jobs"])
api_router.include_router(result.router, tags=["result"])
