FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN mkdir /app/html

CMD ["python3", "./main.py"]
