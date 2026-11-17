
FROM python:3.12-slim

WORKDIR /app

COPY requirements-api.txt .

RUN python -m pip install --no-cache-dir -r requirements-api.txt

COPY app.py calculator.py ./

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
