FROM python:3.12.1-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update && apt-get install -y gcc

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
 pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN chmod +x deployment/worker-entrypoint.sh \
    && chmod +x deployment/server-entrypoint.sh

EXPOSE 8000