FROM python:latest


WORKDIR /app

RUN pip install watchdog
RUN pip install Flask
RUN pip install requests

#ENV fprocess="python3 Service2.py"
COPY ./Service2.py .

EXPOSE 5000
CMD [ "python", "./Service2.py" ]