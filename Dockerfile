FROM node:20-alpine3.18

# alpine에서 사용하는 패키지 관리자의 이름(apk)
RUN apk add --no-cache py3-pip
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev

RUN ln -sf python3 /usr/bin/python3

WORKDIR /code
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

ENTRYPOINT ["ash"]