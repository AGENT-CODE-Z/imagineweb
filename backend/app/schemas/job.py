from pydantic import BaseModel

from .common import JobState


class JobStatusResponse(BaseModel):
    job_id: str
    status: JobState
