from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
)

class UserSerializer(ModelSerializer):
    password = serializers.CharField(max_length=100,
                                     style={'input_type': 'password'},
                                     required=True, write_only=True)


    def create(self,validate_data):
        user = User.objects.create(username=validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('username', 'password')
