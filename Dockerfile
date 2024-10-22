FROM docker.io/python:3.13.0

ARG email="htamayo@netskope.com"
LABEL "maintainer"=$email

USER root

ENV AP=/data/app
RUN mkdir -p /data/app
RUN pip install requests
# App code
COPY ./scim/* $AP

WORKDIR $AP

CMD ["python3", "menu.py"]

