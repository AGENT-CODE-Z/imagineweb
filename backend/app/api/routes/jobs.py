from fastapi import APIRouter, HTTPException, status

from ...schemas.job import JobStatusResponse
from ...services.storage import get_job_status

router = APIRouter()


@router.get("/jobs/{job_id}", response_model=JobStatusResponse, summary="Get job status")
async def read_job_status(job_id: str) -> JobStatusResponse:
    job = get_job_status(job_id)
    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job '{job_id}' was not found.",
        )

    return JobStatusResponse(**job)
