from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from .serializers import UserSerializer

class UserListView(CreateAPIView):
    """
    Class that queries the user model, and map the user object with it's serializers
    We access backend filters
    permission_classes = [AllowAny] to allow others to access this url
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
