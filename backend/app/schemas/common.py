from typing import Literal

from pydantic import BaseModel

JobState = Literal["queued", "processing", "done", "failed"]


class HealthResponse(BaseModel):
    status: str
    service: str


class ErrorResponse(BaseModel):
    detail: str
