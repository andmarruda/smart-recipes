def portuguesePrompt(text: str) -> str:
    return f"""
Você receberá o texto de uma receita culinária.

Sua tarefa é converter esse texto em um JSON estruturado no formato:

{{
  "items": [
    {{
      "amount": number|null,
      "unit": string|null,
      "ingredient": string
    }}
  ],
  "prepareMode": "string"
}}

Regras:
- Identifique corretamente quantidade (amount), unidade (unit) e ingrediente.
- Se não houver quantidade, use amount = null e unit = null.
- Ingrediente deve ser sempre preenchido.
- prepareMode deve conter o modo de preparo descrito no texto.
- Retorne SOMENTE JSON válido, sem comentários, explicações ou texto extra.
- Se a receita não tiver ingredientes, devolva "items": [] e preencha apenas "prepareMode".
- Use unidades em português (ex: "colher de sopa", "xícara", "pitada", "ml", "g").

Texto da receita:
\"\"\"{text}\"\"\"

Saída em JSON apenas:
"""

def englishPrompt(text: str) -> str:
    return f"""
You will receive the text of a cooking recipe.

Your task is to convert this text into a structured JSON in the format:

{{
  "items": [
    {{
      "amount": number|null,
      "unit": string|null,
      "ingredient": string
    }}
  ],
  "prepareMode": "string"
}}

Rules:
- Correctly identify amount, unit, and ingredient.
- If there is no amount, use amount = null and unit = null.
- Ingredient must always be filled.
- prepareMode must contain the preparation instructions described in the text.
- Return ONLY valid JSON, with no comments, explanations, or extra text.
- If the recipe has no ingredients, return "items": [] and only fill "prepareMode".
- Use units in English (e.g., "tablespoon", "cup", "pinch", "ml", "g").

Recipe text:
\"\"\"{text}\"\"\"

JSON output only:
"""
