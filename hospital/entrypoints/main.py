import uvicorn
from fastapi import FastAPI
from hospital.bootstrap import bootstrap
from hospital.entrypoints.views import patients
import uuid

# Create a standard FastAPI app without the custom OpenAPI URL
app = FastAPI(
    title="Hospital Management System",
    description="HMS API",
    version="0.1.0"
)
bus = bootstrap()

app.include_router(patients.router, prefix="/patients", tags=["patients"])

if __name__ == "__main__":
    print("Starting with fresh imports")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)