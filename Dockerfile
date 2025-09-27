FROM python:3.12

# Install system dependencies: Tesseract OCR, compilers, etc.
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
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY config/requirements.txt /app/requirements.txt
RUN CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" \
    python3 -m pip install --force-reinstall --upgrade --no-cache-dir -r /app/requirements.txt

# Copy project files
COPY . .

# Clean up requirements copy inside the container
RUN rm -f /app/config/requirements.txt

# Download model if it does not exist
RUN mkdir -p /app/models && \
    if [ ! -f /app/models/qwen2.5-0.5b-instruct-q4.gguf ]; then \
      curl -L -o /app/models/qwen2.5-0.5b-instruct-q4.gguf \
      https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4.gguf; \
    fi

# Expose port for Flask or API
EXPOSE 8080

# Default command
CMD ["python", "app.py"]
