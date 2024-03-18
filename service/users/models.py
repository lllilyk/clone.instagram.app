from django.db import models
# 아래 두 개의 의존성은 꼭 포함시켜야만 원하는 모델을 구현할 수 있다함
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# 정의할 메소드는 2개
# 장고에서 제공해주는 유저 모델을 사용하는 경우에는 사실 따로 정의할 필요가 없음
# 근데 내가 사용자를 구별하기 위한 유일한 필드로 email을 지정했으므로 이메일을 입력받아서 회원가입할 수 있도록 create_user, create_superuser를 재정의해서 사용해야 함
class UserManager(BaseUserManager):
    # 일반 유저
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # 슈퍼 유저
    def create_superuser(self, eamil, password, **extra_fields):
        extra_fields.set_default('is_staff', True)
        extra_fields.set_default('is_superuser', True)
        extra_fields.set_default('is_active', True)
        return self.create_user(email, password, **extra_fields)


# Create your models here.(모델 정의)
# class User(models.Model): //이렇게 하지 않고 사용자 정보를 다루는 모델을 정의하기 위해서 아래와 같이 작성함
class User(AbstractUser):
    TIMEOUT = 60 * 5
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    profile = models.ImageField(null=False, blank=True)
    description = models.CharField(max_length=512, blank=True)
    authcode = models.CharField(max_length=17)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 이름은 objects가 아니여도 됨
    objects = UserManager()

    class Meta:
        ordering = ['created']
