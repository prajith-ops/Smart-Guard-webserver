from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class LockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lock
        fields='__all__'


class UserLockAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLockAccess
        fields='__all__'


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=SensorData
        fields='__all__'


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alert
        fields='__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid login credentials")
        else:
            raise serializers.ValidationError("Both fields are required")

        data['user'] = user
        return data