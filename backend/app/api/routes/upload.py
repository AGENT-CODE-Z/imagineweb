from fastapi import APIRouter, File, HTTPException, UploadFile, status

from ...core.config import settings
from ...schemas.upload import UploadResponse
from ...services.storage import save_upload

router = APIRouter()


@router.post("/upload", response_model=UploadResponse, summary="Upload a screenshot")
async def upload_screenshot(file: UploadFile = File(...)) -> UploadResponse:
    try:
        uploaded = await save_upload(file, settings.uploads_dir)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return UploadResponse(**uploaded)
