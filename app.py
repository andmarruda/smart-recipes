from flask import Flask, request, jsonify
from dotenv import load_dotenv
from src.ocr import processImage
from src.nlp import processNlp

load_dotenv()
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10485760

ALLOWED_MIME = {"image/jpeg", "image/png", "image/webp"}
LANG_MAP = {"en": "eng", "pt": "por"}
LANG_ALLOWED = LANG_MAP.keys()

def error (msg, code=400):
    return jsonify({"ok": False, "error": msg}), code

@app.route("/", methods=["POST"])
def execute():
    lang = request.form.get("lang", "").strip().lower()
    if lang not in LANG_ALLOWED:
        return error("Invalid language. Use en for English or pt for Portuguese.")

    file = request.files.get("picture")
    if not file:
        return error("Please send your recepie picture to continue.")

    if file.mimetype not in ALLOWED_MIME:
        return error("Please send your recepie picture in jpg, png or webp.")

    processedImage = processImage(file, LANG_MAP[lang])
    if not processedImage["success"]:
        return error(processedImage["error"])

    processedNlp = processNlp(processedImage["text"], LANG_MAP[lang])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)