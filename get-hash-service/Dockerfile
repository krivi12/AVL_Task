FROM python:latest

WORKDIR /app

RUN pip install watchdog
RUN pip install Flask

#ENV fprocess="python3 Service1.py"
COPY ./Service1.py .

EXPOSE 5000
CMD [ "python", "./Service1.py" ]