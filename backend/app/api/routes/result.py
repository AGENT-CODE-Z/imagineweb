from fastapi import APIRouter, HTTPException, status

from ...schemas.result import ResultResponse
from ...services.storage import get_job_result

router = APIRouter()


@router.get("/result/{job_id}", response_model=ResultResponse, summary="Get placeholder result")
async def read_job_result(job_id: str) -> ResultResponse:
    result = get_job_result(job_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job '{job_id}' was not found.",
        )

    return ResultResponse(**result)
