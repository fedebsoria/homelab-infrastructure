# 15. Dockerfile Construction & Analysis

## 📅 Date: 2025-12-02

## 📝 Summary
We analyzed and constructed the `Dockerfile` for the Python Application service. We broke down the file instruction by instruction to understand the concepts of Base Images, Layers, Caching, and Entry Commands.

## ⚙️ Dockerfile Components Explained

### 1. Base Image (`FROM python:3.11-slim`)
We chose the `slim` variant over `alpine` or the full image.
- **Reason:** It provides a balance between size and compatibility (glibc support) required for many Python data science/database libraries.

### 2. Layer Caching Strategy
We separated the dependency installation from the code copying.
- **Step A:** `COPY requirements.txt .` then `RUN pip install ...`
- **Step B:** `COPY . .`
- **Why:** Docker caches layers. If we change `main.py` but not `requirements.txt`, Docker skips Step A (reusing the cache) and only rebuilds Step B. This drastically speeds up build times during development.

### 3. Dev-Mode Entrypoint (`CMD`)
We set the command to `["sleep", "infinity"]`.
- **Reason:** Since the application logic (`main.py`) is under active development, a standard execution command might crash the container if the script has errors. Using sleep keeps the container alive ("Running" status), allowing us to shell into it (`docker exec`) and run the script manually for debugging.