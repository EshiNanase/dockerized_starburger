FROM python:3.9
LABEL maintainer='eshinanase'

COPY ./requirements.txt /tmp/requirements.txt
COPY .env /app/.env

RUN python -m venv . && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

COPY . /app
WORKDIR /app

CMD ["python", "manage.py", "runserver"]
