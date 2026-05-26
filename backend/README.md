# ImagineWeb Backend

This backend is the `Sprint 0` FastAPI foundation for the screenshot-to-website pipeline.

It currently provides:
- a running FastAPI app
- versioned API routes under `/api/v1`
- image upload handling
- temporary in-memory job tracking
- placeholder result output for future OCR, UI detection, and layout modules

## Backend Purpose

The backend acts as the controller for the full pipeline:

1. receive a screenshot from the frontend
2. create a `job_id`
3. store the uploaded image
4. expose job status
5. expose a placeholder result response

In later sprints, OCR, detection, layout understanding, and code generation will plug into this structure.

## Current Folder Structure

```text
backend/
  app/
    main.py
    api/
      routes/
        health.py
        upload.py
        jobs.py
        result.py
        routes.py
    core/
      config.py
    schemas/
      common.py
      job.py
      upload.py
      result.py
    services/
      storage.py
  requirements.txt
  README.md
```

## What Each Part Does

- `app/main.py`
  Starts FastAPI, enables CORS, and mounts all routes under `/api/v1`.

- `app/api/routes/health.py`
  Health-check endpoint to confirm the backend is running.

- `app/api/routes/upload.py`
  Accepts screenshot uploads from the frontend.

- `app/api/routes/jobs.py`
  Returns current job status for a given `job_id`.

- `app/api/routes/result.py`
  Returns placeholder output for a given `job_id`.

- `app/api/routes/routes.py`
  Combines all route modules into one API router.

- `app/core/config.py`
  Stores backend configuration such as API prefix, allowed frontend origin, and upload path.

- `app/schemas/*.py`
  Defines response models used by FastAPI and Swagger docs.

- `app/services/storage.py`
  Handles upload saving, file validation, and temporary in-memory job data.

## Requirements

- `Python 3.10+`
- project virtual environment at repo root: `.venv`

Install backend dependencies with:

```powershell
cd D:\imagineweb\imagineweb
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
```

## How To Run The Backend

From the project root:

```powershell
cd D:\imagineweb\imagineweb
.\.venv\Scripts\Activate.ps1
uvicorn backend.app.main:app --reload
```

The backend runs at:

- `http://127.0.0.1:8000`

Useful URLs:

- Swagger docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/api/v1/health`

## Frontend Integration

The frontend is expected to call:

- `http://localhost:8000/api/v1`

Current allowed frontend origin:

- `http://localhost:5173`

This is configured in `app/core/config.py`.

## API Routes

### `GET /api/v1/health`

Purpose:
- verify the backend is running

Example response:

```json
{
  "status": "ok",
  "service": "imagineweb-backend"
}
```

### `POST /api/v1/upload`

Purpose:
- receive a screenshot image from the frontend

Accepted file types:
- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

What it does:
- validates the file extension
- rejects empty files
- generates a `job_id`
- stores the file in the repo-level `uploads/` folder
- returns upload metadata

Example response:

```json
{
  "job_id": "job_ab12cd34",
  "status": "queued",
  "filename": "sample.png"
}
```

### `GET /api/v1/jobs/{job_id}`

Purpose:
- return the current status of a job

Current behavior:
- uploaded jobs return `queued`
- unknown jobs return `404`

Example response:

```json
{
  "job_id": "job_ab12cd34",
  "status": "queued"
}
```

### `GET /api/v1/result/{job_id}`

Purpose:
- return a placeholder result structure for a completed job

Current behavior:
- known jobs return placeholder page, OCR, and UI data
- unknown jobs return `404`

Example response:

```json
{
  "job_id": "job_ab12cd34",
  "status": "done",
  "result": {
    "page": {
      "sections": []
    },
    "ocr_blocks": [],
    "detected_elements": []
  }
}
```

## Upload Storage

Uploaded files are saved in:

- [uploads](/D:/imagineweb/imagineweb/uploads)

Stored filenames are generated from the `job_id`.

## Current Backend Limitations

This is still a `Sprint 0` foundation, so the backend does not yet include:

- OCR integration
- YOLO or UI detection integration
- layout grouping logic
- generated code output
- persistent database storage
- authentication
- background job queue

## Important Implementation Note

Job data is currently stored in memory inside `app/services/storage.py`.

That means:
- restarting the backend clears job history
- uploaded files remain on disk
- job tracking is only temporary for now

This is acceptable for Sprint 0, but later sprints should replace this with more persistent state management.

## Shared Schema Alignment

The backend follows the shared schema direction from:

- `shared/schemas/README.md`
- `shared/schemas/job.schema.json`
- `shared/schemas/output.schema.json`

Important conventions already followed:

- use `job_id`
- use `status`
- status values are `queued`, `processing`, `done`, `failed`

## Demo Checklist

Before showing the backend to teammates:

1. Start the FastAPI server.
2. Open `/docs`.
3. Test `/api/v1/health`.
4. Upload an image through `/api/v1/upload`.
5. Copy the returned `job_id`.
6. Test `/api/v1/jobs/{job_id}`.
7. Test `/api/v1/result/{job_id}`.

## Handoff Notes For Teammates

Share these details with the team:

- backend base URL: `http://localhost:8000/api/v1`
- frontend dev origin: `http://localhost:5173`
- upload endpoint is ready
- job polling endpoint is ready
- placeholder result endpoint is ready
- uploads are saved in the repo-level `uploads/` folder
