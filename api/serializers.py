from rest_framework import serializers
from django.contrib.auth import authenticate

#app usuario
from usuario.models import CustomerUser

#app aparcamiento
from aparcamiento.models import Aparcamiento


#serializers para usuario
class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = (
            'id',
            'username',
            'email',
            'bancaria',
            'telefono',
            'direccion'
        )

class RegisterCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = (
            'id',
            'username',
            'email',
            'password',
            'bancaria',
            'telefono',
            'direccion'
        )

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validate_data):
        user = CustomerUser.objects.create_user(
            validate_data['username'],
            validate_data['email'],
            validate_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data) #<- los datos obtenidos de username y password

        print("Usuario -> " + str(user)) #debug
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Error de credenciales")

#serializers para aparcamiento
class AparcamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aparcamiento
        fields = (
            'id',
            'direccion',
            'descripcion'
        )