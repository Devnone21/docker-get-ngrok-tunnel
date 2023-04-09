FROM python:3.9-slim-buster

WORKDIR /app

COPY main.py .

RUN mkdir /app/html

# RUN pip install requests beautifulsoup4 python-dotenv

CMD ["python3", "./main.py"]
