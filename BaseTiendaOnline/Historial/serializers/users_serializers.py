import re

from rest_framework import serializers

from Historial.models import Usuarios, RolChoises


class UsersSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=30, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=254, allow_null=False, allow_blank=False)
    telefono = serializers.CharField(required=False,max_length=11, allow_null=True, allow_blank=True)
    nie = serializers.CharField(max_length=10, allow_null=False, allow_blank=False)
    nc = serializers.CharField(required=False,max_length=10, allow_null=True, allow_blank=True)


    password1 = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=4)
    password2 = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=4)
    fecha_nacimiento = serializers.CharField(allow_null=False, allow_blank=False)
    edad = serializers.IntegerField(max_value=120, allow_null=False)

    rol = serializers.ChoiceField(
        choices=RolChoises.choices,
        default=RolChoises.PACIENTE,
        error_messages={"ROL_Invalido": "El Rol Ingresado no es valido"}
    )
    class Meta:
        model = Usuarios
        fields = ('email',
                  'nombre',
                  'password1',
                  'password2',
                  'telefono',
                  'edad',
                  'nie',
                  'nc',
                  'fecha_nacimiento',
                  'rol',)

    def validate_email(self, email):
        if re.search(r"^(?=.*\s)$", email):
            raise serializers.ValidationError("No se permiten espacios en el Email")
        if not re.search(r"^[a-zA-Z\d]+@(gmail|outlook|hotmail|icloud)[a-zA-Z\d.]+$", email):
            raise serializers.ValidationError("Este email tiene una dirección invalida (solo se permiten gmail, outlook, hotmail y icloud)")
        if not re.search(r"^[a-zA-Z\d.@]+\.(es|com)$", email):
            raise serializers.ValidationError("Este email tiene un formato no valido (solo se permiten .es o .com)")
        return email

    def validate_password1(self, password):
        if re.search(r"^(?=.*\s)$", password):
            raise serializers.ValidationError("No se permiten espacios en la Contraseña")
        if not re.search(r"^.{4,}$", password):
            raise serializers.ValidationError("La contraseña debe tener al menos 4 dígitos")
        if not re.search(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$", password):
            raise serializers.ValidationError("La contraseña debe contener al menos 1 numero y al menos 1 letra ")
        return password

    def validate_nie(self,nie):
        if re.search(r"^(?=.*\s)$", nie):
            raise serializers.ValidationError("No se permiten espacios en el NIE")
        if not re.search(r"^([XYZ])(\d{7})([A-Z]+)$", nie):
            raise serializers.ValidationError("El NIE no cumple con los parámetros")
        if Usuarios.objects.filter(nie=nie).exists():
            raise serializers.ValidationError("El NIE ya está registrado.")
        return nie

    def validate_telefono(self,telefono):
        if telefono in [None, ""]:
            return telefono
        try:
            int(telefono)
            return telefono
        except ValueError:
            raise serializers.ValidationError("El teléfono no es valido.")

    def validate_nc(self,nc):
        if nc in [None, ""] and Usuarios.rol != "DOC":
            return nc
        if nc in [None, ""] and Usuarios.rol == "DOC":
            raise serializers.ValidationError("El NC no puede estar vacio.")
        if re.search(r"^(?=.*\s)$", nc):
            raise serializers.ValidationError("No se permiten espacios en el Numero de Colegiatura")
        if not re.search(r"^([0-9]{9})$", nc):
            raise serializers.ValidationError("El Numero de Colegiatura no es valido.")
        if Usuarios.objects.filter(nc=nc).exists():
            raise serializers.ValidationError("El Número de Colegiatura ya está registrado.")
        return nc


    def validate(self,attrs):# ATTRS es un dicionario que contiene todos los datos anteriores
        print( attrs["password1"])
        print(attrs["password2"])
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password1")
        user = Usuarios.objects.create(
            email=validated_data["email"],
            nombre=validated_data["nombre"],
            telefono=validated_data["telefono"],
            nie=validated_data["nie"],
            nc=validated_data["nc"],
            fecha_nacimiento=validated_data["fecha_nacimiento"],
            edad=validated_data["edad"],
            rol=validated_data["rol"]
        )
        user.set_password(password)
        user.save()
        return user