# Approach

The goal of this project is to design a backend service that can extract useful academic information from a marksheet image or document and return it in a structured format.

The focus of this assignment is on **system design, modularity, and clarity of approach**, rather than perfect OCR accuracy.

---

## Overall Flow

The system follows a simple and clear pipeline:

1. Input document upload
2. OCR-based text extraction
3. Rule-based parsing of extracted text
4. (Optional) Normalization step
5. Structured JSON output

Each step is kept independent so that it can be improved or replaced later without affecting the entire system.

---

## OCR Layer

The OCR step is responsible for converting the uploaded marksheet (image or PDF) into raw text.

This logic is isolated inside a dedicated OCR service module. Keeping OCR separate allows:
- Easy replacement of the OCR engine
- Independent debugging
- Clear separation of concerns

At this stage, the OCR output is treated as unstructured text.

---

## Parsing Layer

The parsing layer takes the raw OCR text and attempts to extract meaningful information such as:
- Candidate name
- Roll number
- Subject names
- Marks obtained

This is done using simple rule-based and keyword-based logic.  
The aim here is not to handle every possible format, but to demonstrate how raw OCR output can be converted into structured data.

---

## Normalization Layer

A normalization layer is designed to clean and standardize the parsed data.

This step can optionally use an LLM or other intelligent logic to:
- Normalize subject names
- Handle minor inconsistencies
- Improve output consistency

For security and simplicity, API keys are not hardcoded and this layer is kept optional.

---

## API Design

FastAPI is used to expose the functionality as a REST API.

- A single `/extract` endpoint is provided
- The API accepts a file upload
- The response is returned in JSON format
- Swagger documentation is available via `/docs`

This makes the system easy to test and extend.

---

## Design Principles Followed

- Modular code structure
- Clear separation of responsibilities
- Easy extensibility
- Security-first approach (no secrets in code)

---

## Conclusion

This project demonstrates a practical backend design for document processing using OCR and parsing techniques.  
The emphasis is on clean architecture and thoughtful design rather than complex model tuning.
