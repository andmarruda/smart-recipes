from src/prompt import portuguesePrompt, englishPrompt
from llama_cpp import Llama
import os

def processNlp(text, lang):
    llm = Llama(
        model_path="./models/qwen2.5-0.5b-instruct-q4.gguf",
        n_threads=int(os.getenv("LLM_THREADS", 4)),
        n_ctx=int(os.getenv("LLM_CTX", 2048))
    )

    prompt = portuguesePrompt(text) if lang == "pt" else englishPrompt(text)
    response = llm(
        prompt,
        max_tokens=int(os.getenv("LLM_MAX_TOKENS", 200)),
    )

    print(response)
