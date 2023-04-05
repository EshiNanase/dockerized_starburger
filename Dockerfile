FROM node:16.16.0 as static
LABEL maintainer='eshinanase'

WORKDIR /app

COPY assets /app/assets
COPY bundles-src /app/bundles-src
COPY package.json /app

RUN npm i && \
    ./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"

FROM python:3.9
LABEL maintainer='eshinanase'

WORKDIR /app

COPY backend/. /app
COPY requirements.txt /tmp/requirements.txt
COPY wait-for-it.sh /app

RUN python -m venv . && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    chmod +x wait-for-it.sh

COPY --from=static /app /app
