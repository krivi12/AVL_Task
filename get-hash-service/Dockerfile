FROM python:latest

WORKDIR /app

COPY ./Service1.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "./Service1.py" ]
