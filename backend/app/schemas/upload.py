from pydantic import BaseModel

from .common import JobState


class UploadResponse(BaseModel):
    job_id: str
    status: JobState
    filename: str
