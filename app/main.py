from fastapi import FastAPI
from app.routes.extract import router as extract_router

app = FastAPI(
    title="Marksheet Extraction API",
    description="Extracts structured data from marksheets",
    version="1.0.0"
)

app.include_router(extract_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "API is running"}
