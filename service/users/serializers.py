# model serializer 생성
from rest_framework import serializers

from models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Serializer의 쓰임
        # 1. 객체를 전달하면 해당 객체에 JSON 표현을 반환
        # 이 serializers는 User 필드에 있는 데이터들로 JSON을 생성하게 해줌.
        model = User
        field = (
            'pk',
            'email',
            'username',
            'profile',
            'description',
            'password',
            'updated'
        )
        extra_kwards = {
            'password': {
                'write_only': True
            }
        }
    
    # 2. JSON 형태의 데이터를 제공하면 isValid를 수행해서 save한 후 그 데이터를 가지고 객체를 생성함
    # 앞서 정의한 manager에 create_user를 사용해 사용자 객체를 생성하여 반환하도록 정의
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    # update의 경우에는 django에서 만들어주는 메서드 그냥 사용해도 됨
