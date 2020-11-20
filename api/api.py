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
    CustomerUserSerializer,
    RegisterCustomSerializer,
)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterCustomSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "custom_user":CustomerUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })