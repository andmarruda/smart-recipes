from src.prompt import portuguesePrompt, englishPrompt
from llama_cpp import Llama, LlamaGrammar
import os, re, json

RECIPE_JSON_SCHEMA = {
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "amount": {"type": ["number", "null"]},
          "unit": {"type": ["string", "null"]},
          "ingredient": {"type": "string"},
          "note": {"type": ["string", "null"]}
        },
        "required": ["amount", "unit", "ingredient", "note", "sourceLine"],
        "additionalProperties": False
      }
    },
    "prepareMode": {"type": "string"}
  },
  "required": ["items", "prepareMode"],
  "additionalProperties": False
}

RECIPE_GRAMMAR = LlamaGrammar.from_json_schema(json.dumps(RECIPE_JSON_SCHEMA))

def extract_json(text: str):
    m = re.search(r"\{.*\}\s*\Z", text, flags=re.S)
    if not m:
        raise ValueError("JSON não encontrado")
    return json.loads(m.group(0))

def processNlp(text: str, lang: str):
    model_path = os.getenv("LLM_MODEL_PATH", "/app/src/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf")
    llm = Llama(
        model_path=model_path,
        n_threads=int(os.getenv("LLM_THREADS", 4)),
        n_ctx=int(os.getenv("LLM_CTX", 2048))
    )

    prompt = portuguesePrompt(text) if lang == "pt" else englishPrompt(text)

    resp = llm(
        prompt,
        max_tokens=int(os.getenv("LLM_MAX_TOKENS", 700)),
        temperature=float(os.getenv("LLM_TEMPERATURE", 0.3)),
        top_p=float(os.getenv("LLM_TOP_P", 0.9)),
        grammar=RECIPE_GRAMMAR
    )

    raw = resp["choices"][0]["text"]
    data = extract_json(raw)
    return {"success": True, "json": data}
