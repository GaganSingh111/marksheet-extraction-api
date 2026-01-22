# Marksheet Extraction API

A FastAPI-based backend service for extracting structured information from marksheet images using OCR and rule-based parsing.

This project focuses on API design, modular architecture, and clear documentation rather than perfect OCR accuracy.

## Features
- FastAPI backend with Swagger docs
- OCR-based text extraction
- Parsing into structured JSON
- Modular services (OCR, parsing, normalization-ready)

## Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
