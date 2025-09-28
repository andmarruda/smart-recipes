# Smart Recipes – From Raw Text to Structured Culinary Data

## 🍲 The Story Behind Smart Recipes

Cooking is universal, but recipes are messy.  
They come in **handwritten notes, blurry images, PDFs, and blog posts** full of personal anecdotes. What if we could **turn any recipe into clean, structured, machine-readable data**—ready to power apps, nutrition calculators, search engines, or even AI assistants?

That’s exactly what **Smart Recipes** was built for.  

It’s not just an OCR and NLP pipeline—it’s a bridge between human creativity in the kitchen and structured knowledge that machines can understand.

---

## 🚀 What Smart Recipes Does

- 📸 **Reads recipes from images** with Tesseract OCR (yes, even messy scans).  
- 🌍 **Understands multiple languages** (currently Portuguese 🇧🇷 and English 🇺🇸).  
- 🧠 **Normalizes fractions and units** (`1/2 cup → 0.5`, `1 colher (sopa) → tablespoon`).  
- 🍅 **Splits every ingredient into its own structured entry**.  
- 📝 **Extracts the preparation steps** without noise.  
- ✅ **Validates against a strict JSON schema** so the output is always predictable.  

The result?  
A recipe that a human can cook **and** a machine can reason about.

---

## 🧩 Why It Matters

- **For developers**: Build recipe apps, meal planners, or grocery list generators with consistent data.  
- **For data scientists**: Feed models with normalized food datasets instead of chaotic text.  
- **For companies**: Unlock content pipelines, SEO opportunities, and even personalized nutrition recommendations.  

This project is where **culinary culture meets machine intelligence**.

---

## ⚙️ How It Works

1. **OCR Layer** – Uses `pytesseract` + `Pillow` to extract raw text from images.  
2. **NLP Layer** – Runs the text through `llama-cpp-python` with a carefully designed **grammar-constrained prompt**.  
3. **Validation** – Ensures the output matches the strict JSON schema:
   ```json
   {
     "items": [
       {
         "amount": 500,
         "unit": "g",
         "ingredient": "ground beef",
         "note": "double minced"
       }
     ],
     "prepareMode": "Mix ingredients, form into patties, and grill."
   }
````

4. **Clean Separation** – Ingredients, units, and preparation steps are always distinct. No messy overlaps.

---

## 🛠️ Tech Stack

* **Python 3.12**
* **llama-cpp-python** for local LLM inference
* **Pillow** & **pytesseract** for OCR
* **Tesseract OCR** (system dependency)
* **JSON Schema** for guaranteed structure

---

## 🧑‍💻 Quickstart

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourname/smart-recipes.git
cd smart-recipes
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make sure Tesseract OCR is installed:

```bash
sudo apt-get install tesseract-ocr
```

Run a quick test:

```python
from src.ocr import processImage
from src.nlp import processNlp

# OCR from image
with open("recipe.jpg", "rb") as f:
    print(processImage(f, lang="eng"))

# NLP from raw text
text = "500g ground beef, 1 cup bulgur wheat, juice of 1 lemon..."
print(processNlp(text, lang="en"))
```

---

## 🌟 Why This Project Stands Out

There are plenty of OCR tools. There are plenty of NLP projects.
But **Smart Recipes** combines both into a **real-world, domain-specific pipeline**:

* **Precision**: Grammar-constrained JSON means no “hallucinations”.
* **Practicality**: Focused on recipes, not generic text.
* **Scalability**: Works offline, with your own LLMs.
* **Creativity**: It’s not just about parsing text—it’s about turning culture into data.

---

## 📌 Use Cases

* 🍳 Personal cooking assistant apps
* 🛒 Automatic grocery list generators
* 📈 Nutritional analysis dashboards
* 🔎 Recipe search engines with structured filters
* 🤖 AI-driven meal planning

---

## 📜 License

MIT License – free to use, free to adapt, free to improve.

---

## ✨ Final Note

Smart Recipes is more than code.
It’s a demonstration of **how thoughtful prompt design, schema validation, and OCR can turn messy human input into structured intelligence**.

If you’re a recruiter, CTO, or fellow developer reading this:
this project is proof that I don’t just write code—I **design systems that solve real, human problems**.