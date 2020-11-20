from rest_framework import serializers
from django.contrib.auth import authenticate

#app
from usuario.models import CustomerUser

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
        user = CustomerUser.objects.create(
            **validate_data
        )
        return user