from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ocr_service import run_ocr
from app.services.parsing_service import parse_marksheet
from app.services.llm_service import normalize_with_llm

router = APIRouter()

@router.post("/extract")
async def extract_marksheet(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png", "application/pdf"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    file_bytes = await file.read()

    ocr_output = run_ocr(file_bytes, file.content_type)
    if not ocr_output:
        raise HTTPException(status_code=422, detail="No text detected")

    parsed_data = parse_marksheet(ocr_output)
    normalized_data = normalize_with_llm(parsed_data)

    return {
        "normalized_data": normalized_data
    }
