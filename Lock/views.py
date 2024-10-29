from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class LockViewSet(viewsets.ModelViewSet):
    queryset=Lock.objects.all()
    serializer_class=LockSerializer


class UserLockAccessViewSet(viewsets.ModelViewSet):
    queryset=UserLockAccess.objects.all()
    serializer_class=UserLockAccessSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset=SensorData.objects.all()
    serializer_class=SensorDataSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset=Alert.objects.all()
    serializer_class=AlertSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)  # Generate JWT token
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

