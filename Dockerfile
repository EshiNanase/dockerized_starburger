FROM node:16.16.0 as static
LABEL maintainer='eshinanase'

WORKDIR /app/frontend

COPY frontend/assets /app/frontend/assets
COPY frontend/bundles-src /app/frontend/bundles-src
COPY frontend/package.json /app/frontend/

RUN npm i && \
    ./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"

FROM python:3.9
LABEL maintainer='eshinanase'

WORKDIR /app

COPY backend/. /app
COPY requirements.txt /tmp/requirements.txt

RUN python -m venv . && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

COPY --from=static /app/frontend /app
