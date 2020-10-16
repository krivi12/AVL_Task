FROM python:latest

RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog
RUN pip install Flask
RUN pip install requests

ENV fprocess="python entrypoint.py"
COPY entrypoint.py /

EXPOSE 8080
CMD [ "fwatchdog" ]