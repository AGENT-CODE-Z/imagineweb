# ImagineWeb

ImagineWeb is a `screenshot-to-website` project. The goal is to take a webpage screenshot, extract its structure, understand the layout, and generate frontend code from it.

This repository is currently in `Sprint 0`, where the team is building the shared foundation for later OCR, detection, layout, and code-generation work.

## Sprint 0 Goal

Sprint 0 is about making the project buildable and shareable across the team.

Current focus areas:
- frontend foundation
- backend foundation
- shared schemas
- architecture and documentation
- sample inputs and outputs

## Current Project Structure

```text
imagineweb/
  backend/
  frontend/
  modules/
  outputs/
  samples/
  shared/
  uploads/
```

## Folder Overview

- `backend/`
  FastAPI backend for uploads, job status, and result endpoints.

- `frontend/`
  React + Vite frontend application.

- `modules/`
  Reserved folders for future OCR, UI detection, layout, and code-generation logic.

- `samples/`
  Shared sample inputs and expected example outputs.

- `shared/`
  Shared schemas and contracts used across modules.

- `uploads/`
  Local storage for uploaded screenshots during development.

- `outputs/`
  Reserved location for generated outputs in later sprints.

## Current Status

What is already done:
- frontend scaffold exists in `frontend/vision2web-from-scratch`
- backend scaffold exists in `backend/app`
- shared schema files exist in `shared/schemas`
- backend upload, job, result, and health routes are working
- backend documentation and requirements are available in `backend/`

What is still left before Sprint 0 is fully complete:
- add real sample screenshots to `samples/input`
- improve top-level architecture and ownership notes as the team finalizes them
- complete frontend-backend integration
- add starter notes or initial code inside `modules/ocr`, `modules/detection`, `modules/layout`, and `modules/codegen`

## Backend

Backend docs are available here:

- [backend/README.md](/D:/imagineweb/imagineweb/backend/README.md)

Backend dependencies are listed here:

- [backend/requirements.txt](/D:/imagineweb/imagineweb/backend/requirements.txt)

Run the backend from the project root:

```powershell
cd D:\imagineweb\imagineweb
.\.venv\Scripts\Activate.ps1
uvicorn backend.app.main:app --reload
```

Backend URLs:
- Swagger docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/api/v1/health`

## Frontend

The frontend app is located here:

- [frontend/vision2web-from-scratch](/D:/imagineweb/imagineweb/frontend/vision2web-from-scratch)

Typical frontend commands:

```powershell
cd D:\imagineweb\imagineweb\frontend\vision2web-from-scratch
npm install
npm run dev
```

## Shared Schemas

Schema files are located here:

- [shared/schemas](/D:/imagineweb/imagineweb/shared/schemas)

Current schema conventions include:
- use `job_id`
- use `status`
- use `x`, `y`, `width`, `height` for bounding boxes

## Team Handoff Notes

For remote collaboration, each sprint owner should document:
- what was completed
- how to run their part locally
- any dependencies added
- what the next person should continue
- known issues or limitations

This is especially important because the team rotates across different project areas each sprint.
