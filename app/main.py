from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.services.genderize import fetch_gender
from app.utils.helpers import process_response

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom error format
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail
        }
    )

@app.get("/api/classify")
async def classify(name: str = Query(None)):
    
    # Validation
    if name is None or name.strip() == "":
        raise HTTPException(status_code=400, detail="Name is required")

    if not isinstance(name, str):
        raise HTTPException(status_code=422, detail="Name must be a string")

    try:
        raw_data = await fetch_gender(name)

        # Edge case handling
        if raw_data.get("gender") is None or raw_data.get("count") == 0:
            return {
                "status": "error",
                "message": "No prediction available for the provided name"
            }

        processed = process_response(raw_data)

        return {
            "status": "success",
            "data": processed
        }

    except Exception:
        raise HTTPException(status_code=502, detail="External API error")
