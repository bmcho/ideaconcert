FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /home/ideaconcert

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
