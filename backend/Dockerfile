FROM python:3.9.0-alpine3.12

COPY requirements.txt /src/app/
WORKDIR /src/app
RUN pip install -r requirements.txt
COPY * /src/app/