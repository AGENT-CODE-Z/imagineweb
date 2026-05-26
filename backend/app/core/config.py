from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    api_prefix: str = "/api/v1"
    cors_origins: list[str] = field(default_factory=lambda: ["http://localhost:5173"])
    repo_root: Path = field(default_factory=lambda: Path(__file__).resolve().parents[3])

    @property
    def uploads_dir(self) -> Path:
        return self.repo_root / "uploads"


settings = Settings()
