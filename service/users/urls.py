# Client 또는 프론트엔드에서의 요청(url)과 정의한 메서드를 연결하기 위함
from django.urls import path

from .views import (
    AuthViewSet
)

# 해당 url에 post 요청이 오면, views.py의 AuthViewSet의 signup 메서드를 사용하겠다는 의미
signup = AuthViewSet.as_view((
    'post': 'signup'
))

urlpatterns = [
    path('/signup', signup)
]

# 실제로 요청을 받는 부분은 지금의 users앱 내 urls.py가 아니라 service 프로젝트의 urls.py임 
# 그니까 service 프로젝트 내 urls.py도 수정해줘야 함