FROM python:3.9-buster

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY website website
COPY server.py server.py
COPY static static
COPY content content
COPY templates templates

ENTRYPOINT ["python", "server.py"]

