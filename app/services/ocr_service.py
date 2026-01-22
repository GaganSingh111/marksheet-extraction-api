import io
import numpy as np
import fitz  # PyMuPDF
from PIL import Image
from paddleocr import PaddleOCR

ocr_engine = PaddleOCR(use_angle_cls=False, lang="en")


def run_ocr(file_bytes: bytes, content_type: str):
    texts = []

    # ---------- CASE 1: PDF ----------
    if content_type == "application/pdf":
        pdf = fitz.open(stream=file_bytes, filetype="pdf")

        for page in pdf:
            pix = page.get_pixmap()
            img_bytes = pix.tobytes("png")

            image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
            image_np = np.array(image)

            result = ocr_engine.ocr(image_np)

            if result and len(result) > 0:
                for line in result[0]:
                    texts.append(line[1][0])

    # ---------- CASE 2: IMAGE ----------
    else:
        image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
        image_np = np.array(image)

        result = ocr_engine.ocr(image_np)

        if result and len(result) > 0:
            for line in result[0]:
                texts.append(line[1][0])

    return texts
