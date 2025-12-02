# 1. Base image: Python 3.11 lite version (debian)
FROM python:3.11-slim
# 2. Define the work directory inside the container
WORKDIR /app
# 3. Copy first the dependencies (for docker cache use)
COPY requirements.txt .
# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# 5. Copy the rest of the code
COPY . .
# 6. Default Command: keep the container on (dev mode)
CMD ["sleep", "infinity"]