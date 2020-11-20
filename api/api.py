#REST_FRAMEWORK
from rest_framework import generics, permissions
from rest_framework.response import Response

#KNOX
from knox.models import AuthToken

#APP USUARIO
from usuario.models import CustomerUser

#APP APARCAMIENTO
from aparcamiento.models import Aparcamiento

#SERIALIZERS
from .serializers import (
    AparcamientoSerializer,
    CustomerUserSerializer,
    LoginSerializer,
    RegisterCustomSerializer,
)

#Register Serializer
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterCustomSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "custom_user":CustomerUserSerializer(user, context=self.get_serializer_context()).data
        })

#Login Serializer
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": CustomerUserSerializer(user, context=self.get_serializer_context()).data,
            "token":token
        })

class ListUserAPI(generics.RetrieveAPIView):
    serializer_class = CustomerUserSerializer
    
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.user



#Aparcamiento Serializer
class ListAparcamientoAPI(generics.ListAPIView):
    serializer_class = AparcamientoSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return Aparcamiento.objects.all()

