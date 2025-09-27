FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    tesseract-ocr-por \
    tesseract-ocr-eng \
    pkg-config \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

COPY config/requirements.txt .
RUN CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" \
    python3 -m pip install --force-reinstall --upgrade --no-cache-dir -r /requirements.txt

COPY . .

RUN rm -f config/requirements.txt

CMD ["python", "app.py"]