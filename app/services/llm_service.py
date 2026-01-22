
'''import os
import openai
openai.api_key = os.getenv("Open_Ai_key")
#def normalize_with_llm(parsed_data: dict) -> dict:
    prompt = f"""
You are given OCR-parsed marksheet data.

Your task:
- Normalize names, dates, and numbers
- Convert subject rows into structured fields
- Do NOT guess missing values
- If a field is unclear, return null
- Output ONLY valid JSON

Input data:
{parsed_data}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data normalization assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content'''

def normalize_with_llm(parsed_data):
    # TEMPORARY SAFE FALLBACK
    return parsed_data
