# django modules
from django.contrib.auth import authenticate
from django.contrib.auth import login

# drf modules
from rest_framework import status
from rest_framework import Response
from rest_framework import ModelViewSets
from rest_framework.permissions import AllowAny

# modules
from users.models import User

# serializers
from users.serializers import UserSerializer

class AuthViewSet(ModelViewSets):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [AllowAny]

    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        login(request, user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        ) 
