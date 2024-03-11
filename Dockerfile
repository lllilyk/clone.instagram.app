FROM docker.io/library/node:20-alpine3.18

RUN apk add --no-cache python3-dev py3-pip postgresql-dev gcc musl-dev jpeg-dev zlib-dev

WORKDIR /code
COPY requirements-dev.txt .

RUN pip3 install --no-cache-dir -r requirements-dev.txt

ENTRYPOINT ["ash"]