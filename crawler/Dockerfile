FROM python:3.10.13-slim-bullseye

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "index.py"]