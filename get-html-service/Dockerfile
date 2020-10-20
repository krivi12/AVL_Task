FROM python:latest

ENV HASH_SERVICE_URL=hash-service

WORKDIR /app

COPY ./Service2.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "./Service2.py" ]