import re

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from Historial.models import Usuarios


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Usuarios
        fields = ('email', 'password')

    def validate_email(self, email):

        if re.search(r"^(?=.*\s)$", email):
            raise serializers.ValidationError("No se permiten espacios en el Email")
        if not re.search(r"^[a-zA-Z\d]+@(gmail|outlook|hotmail|icloud)[a-zA-Z\d.]+$", email):
            raise serializers.ValidationError(
                "Este email tiene una dirección invalida (solo se permiten gmail, outlook, hotmail y icloud)")
        if not re.search(r"^[a-zA-Z\d.@]+\.(es|com)$", email):
            raise serializers.ValidationError("Este email tiene un formato no valido (solo se permiten .es o .com)")
        return email

    def validate_password(self, password):
        if re.search(r"^(?=.*\s)$", password):
            raise serializers.ValidationError("No se permiten espacios en la Contraseña")
        if not re.search(r"^.{4,}$", password):
            raise serializers.ValidationError("La contraseña debe tener al menos 4 dígitos")
        if not re.search(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$", password):
            raise serializers.ValidationError("La contraseña debe contener al menos 1 numero y al menos 1 letra ")
        return password

    def validate(self, attrs):
        user = None
        if attrs.get("email"):
            user = Usuarios.objects.filter(email=attrs['email']).first()
        if not user.check_password(attrs['password']) and user:
            raise serializers.ValidationError({"password": "Contraseña incorrecta"})

        refresh = RefreshToken.for_user(user)
        refresh["nombre"] = user.nombre

        return {
            "success": True,
            "data": {
                "nombre": user.nombre,
                "email": user.email,
                "rol": user.rol,
                "nie": user.nie,
                "refresh_token": str(refresh),
                "token": str(refresh.access_token)
            }
        }
