FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.6.1

WORKDIR /srv/server
 
COPY . /srv/server

RUN apt update  && \
    apt install -y \
    gcc gfortran musl-dev g++ bash wget

# 의존성 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["gunicorn", "--bind", "0:8000", "ideaconcert.wsgi:application"]