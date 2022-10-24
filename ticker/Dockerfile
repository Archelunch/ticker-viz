FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./ticker/requirements.txt .
RUN pip install -r requirements.txt

COPY . /ticker

WORKDIR /ticker

ENTRYPOINT ["./start.sh"]