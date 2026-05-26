from typing import Any

from pydantic import BaseModel, Field

from .common import JobState


class PageModel(BaseModel):
    sections: list[dict[str, Any]] = Field(default_factory=list)


class ResultPayload(BaseModel):
    page: PageModel = Field(default_factory=PageModel)
    ocr_blocks: list[dict[str, Any]] = Field(default_factory=list)
    detected_elements: list[dict[str, Any]] = Field(default_factory=list)


class ResultResponse(BaseModel):
    job_id: str
    status: JobState
    result: ResultPayload
