FROM python:3.10-slim

WORKDIR /app
Copy . .


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]