import io
from PIL import Image, UnidentifiedImageError
import pytesseract
import re

def processImage(file, lang):
    try:
        buf = io.BytesIO(file.read())
        img = Image.open(buf)
        img.verify()
        buf.seek(0)
        img = Image.open(buf).convert("RGB")
    except UnidentifiedImageError:
        return {"success": False, "error": "The file is not a valid image."}
    except Exception:
        return {"success": False, "error": "Unknown error occurred while trying to process the image."}

    try:
        text = pytesseract.image_to_string(img, lang=lang)
    except pytesseract.TesseractError as e:
        return {"success": False, "error": f"Tesseract error: {str(e)}"}

    return {"success": True, "text": text.strip()}
