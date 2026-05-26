from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
_jobs: dict[str, dict[str, str]] = {}


def _validate_filename(filename: str) -> str:
    suffix = Path(filename).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Unsupported file type. Allowed: .png, .jpg, .jpeg, .webp"
        )

    return suffix


async def save_upload(file: UploadFile, uploads_dir: Path) -> dict[str, str]:
    filename = file.filename or "upload.png"
    suffix = _validate_filename(filename)

    file_bytes = await file.read()
    if not file_bytes:
        raise ValueError("Uploaded file is empty.")

    uploads_dir.mkdir(parents=True, exist_ok=True)

    job_id = f"job_{uuid4().hex[:8]}"
    stored_filename = f"{job_id}{suffix}"
    saved_path = uploads_dir / stored_filename
    saved_path.write_bytes(file_bytes)

    _jobs[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "filename": filename,
        "stored_filename": stored_filename,
        "saved_path": str(saved_path),
    }

    return {
        "job_id": job_id,
        "status": "queued",
        "filename": filename,
    }


def get_job_status(job_id: str) -> dict[str, str] | None:
    job = _jobs.get(job_id)
    if job is None:
        return None

    return {
        "job_id": job["job_id"],
        "status": job["status"],
    }


def get_job_result(job_id: str) -> dict[str, object] | None:
    job = _jobs.get(job_id)
    if job is None:
        return None

    return {
        "job_id": job["job_id"],
        "status": "done",
        "result": {
            "page": {
                "sections": [],
            },
            "ocr_blocks": [],
            "detected_elements": [],
        },
    }
