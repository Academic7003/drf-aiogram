FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /bot
WORKDIR /bot
COPY . /bot/

RUN pip install -r aiogram/requirements.txt


