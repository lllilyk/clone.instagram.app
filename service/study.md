Docker 컨테이너 내에서 실행되고 있음
-> 컨테이너 내부에서는 Linux 환경을 사용하고 있으며 Linux 쉘 프롬프트에서 가상 환경을 활성화하고 프로젝트 디렉토리인 /code로 이동한 상태
--> Docker 컨테이너가 이미 실행 중이므로 해당 컨테이너에 접속하여 내부에서 작업하는 것이 좋음

<br />

## Docker 컨테이너에 접속하여 실행중인 쉘 확인
```bash
    docker exec -it instaclone-01 ash
```

<br />

이렇게 Docker 컨테이너 내부 쉘에 접속한 후, 가상 환경을 활성화하고 /code 디렉토리로 이동하여 프로젝트 계속 진행!!

<br />

## 가상 환경 활성화
```bash
    source myenv/bin/activate
```

<br />

## 서버 실행
```bash
    (myenv) /code/service # python manage.py runserver 0.0.0.0:8000
```