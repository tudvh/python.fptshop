FROM python:3.10.13-slim-bullseye

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "index:app", "--port", "8000"]