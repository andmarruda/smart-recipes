def portuguesePrompt(text: str) -> str:
    return f"""
Você receberá o texto de uma receita culinária.

Sua tarefa é converter esse texto em um JSON no formato:

{{
  "items": [
    {{
      "amount": number|null,
      "unit": string|null,
      "ingredient": string,
      "note": string|null
    }}
  ],
  "prepareMode": "string"
}}

Instruções importantes sobre a separação de itens:
- Separe ingrediente por ingrediente. Cada linha do texto que contenha um ingrediente deve resultar em exatamente um item no array.
- Se uma mesma linha contiver vários ingredientes separados por vírgulas, ponto e vírgula ou pela conjunção “e”, divida em múltiplos itens, um por ingrediente.
- Não junte vários ingredientes em um único item.
- Respeite a ordem do texto: os itens devem aparecer no JSON na mesma ordem em que surgem no texto, de cima para baixo.

Regras de extração e normalização:
1) Converta frações para decimal (1/2 → 0.5, 1 1/2 → 1.5).
2) Identifique corretamente amount, unit e ingredient. Se não houver quantidade, use amount=null e unit=null.
3) Ingredient pode ser nome composto, por exemplo "trigo para quibe", "cebola ralada", "folhas de hortelã".
4) Derivados como "suco de 1 limão", "raspas de laranja", "folhas de hortelã":
   - Use o derivado em ingredient e a origem em note.
   - Exemplo: {{ "amount": 1, "unit": null, "ingredient": "suco", "note": "de 1 limão" }}.
5) Para expressões como "a gosto" ou "para decorar": amount=null, unit=null, descreva em note.
6) Normalize unidades: "colher (sopa)", "colher (chá)", "xícara (chá)", "g", "kg", "ml", "l", "pitada".
7) Se a unidade for o próprio ingrediente (ex.: "1/2 cebola", "2 tomates"), deixe unit=null. Não invente medidas de volume ou peso nesses casos.
8) A propriedade `note` deve estar **estritamente ligada apenas ao ingrediente da mesma linha**. Nunca reutilize ou propague notas para outros itens.
9) **Definição de ingrediente**: ingrediente é sempre uma comida ou componente que serve para cozinhar (ex.: cebola, tomate, farinha, leite, ovos). Palavras que são apenas descrições (ex.: "ralada", "picada", "cheia", "inteira") **não são ingredientes** e devem ir no campo `note`.
   - Exemplo correto:  
     Texto: *"1/2 cebola ralada"*  
     JSON: {{ "amount": 0.5, "unit": null, "ingredient": "cebola", "note": "ralada" }}
10) prepareMode deve conter o modo de preparo do texto, limpo de ruído. Não invente passos.
11) Ignore títulos, autor e cabeçalhos. Somente ingredientes entram em items.
12) Responda somente com JSON válido, sem qualquer texto extra.

Texto da receita:
\"\"\"{text}\"\"\" 

JSON:
"""

def englishPrompt(text: str) -> str:
    return f"""
You will receive the text of a cooking recipe.

Your task is to convert this text into a JSON with the format:

{{
  "items": [
    {{
      "amount": number|null,
      "unit": string|null,
      "ingredient": string,
      "note": string|null
    }}
  ],
  "prepareMode": "string"
}}

Critical instructions about item separation:
- Split ingredients item by item. Each line in the text that contains an ingredient must produce exactly one array item.
- If a single line contains multiple ingredients separated by commas, semicolons, or the word “and”, split them into multiple items, one per ingredient.
- Do not pack multiple ingredients into a single item.
- Keep the original order: items must follow the top-to-bottom order they appear in the text.

Extraction and normalization rules:
1) Convert fractions to decimal (1/2 → 0.5, 1 1/2 → 1.5).
2) Correctly identify amount, unit, and ingredient. If no amount is present, use amount=null and unit=null.
3) Ingredient may be compound, for example "bulgur wheat", "grated onion", "mint leaves".
4) Derived items like "juice of 1 lemon", "orange zest", "mint leaves":
   - Put the derivative in ingredient and the source in note.
   - Example: {{ "amount": 1, "unit": null, "ingredient": "juice", "note": "of 1 lemon" }}.
5) For “to taste” or “for garnish”: amount=null, unit=null, describe in note.
6) Normalize units: "tablespoon", "teaspoon", "cup", "g", "kg", "ml", "l", "pinch".
7) If the unit is actually the ingredient itself (e.g. "1/2 onion", "2 tomatoes"), set unit=null. Do not invent volume or weight units in these cases.
8) The `note` field must be **strictly bound only to the ingredient from the same line**. Never reuse or propagate notes to other items.
9) **Definition of ingredient**: an ingredient is always a food item or a cooking component (e.g. onion, tomato, flour, milk, eggs). Words that are only descriptors (e.g. "chopped", "grated", "whole", "heaped") are **not ingredients** and must go into the `note` field.  
   - Correct example:  
     Text: *"1/2 onion, grated"*  
     JSON: {{ "amount": 0.5, "unit": null, "ingredient": "onion", "note": "grated" }}
10) prepareMode must contain the cooking instructions from the text, cleaned from noise. Do not invent steps.
11) Ignore titles, author names and headings. Only ingredients go into items.
12) Return ONLY valid JSON with no extra text.

Recipe text:
\"\"\"{text}\"\"\" 

JSON:
"""
