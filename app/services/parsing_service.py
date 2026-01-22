from typing import List, Dict

def normalize_text(text: str) -> str:
    return text.strip().replace(":", "").lower()
CANDIDATE_KEYWORDS = {
    "name": ["name"],
    "roll_no": ["roll", "roll no", "roll number"],
    "dob": ["dob", "date of birth"],
    "registration_no": ["registration", "reg no"],
    "board": ["board", "university"],
    "year": ["year", "exam year"]
}

RESULT_KEYWORDS = ["result", "division", "grade", "pass", "fail"]
def extract_candidate_details(ocr_lines: List[Dict]) -> Dict:
    candidate = {}

    for line in ocr_lines:
        text = normalize_text(line["text"])

        for field, keywords in CANDIDATE_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    candidate[field] = {
                        "value": line["text"],
                        "confidence": line["confidence"]
                    }

    return candidate
def is_probable_subject_row(text: str) -> bool:
    digits = sum(c.isdigit() for c in text)
    return digits >= 2

def extract_subjects(ocr_lines: List[Dict]) -> List[Dict]:
    subjects = []

    for line in ocr_lines:
        text = line["text"]

        if is_probable_subject_row(text):
            subjects.append({
                "raw_text": text,
                "confidence": line["confidence"]
            })

    return subjects
def extract_result(ocr_lines: List[Dict]) -> Dict:
    for line in ocr_lines:
        text = normalize_text(line["text"])

        for keyword in RESULT_KEYWORDS:
            if keyword in text:
                return {
                    "value": line["text"],
                    "confidence": line["confidence"]
                }

    return {}

def parse_marksheet(ocr_lines: List[Dict]) -> Dict:
    return {
        "candidate": extract_candidate_details(ocr_lines),
        "subjects": extract_subjects(ocr_lines),
        "result": extract_result(ocr_lines)
    }
