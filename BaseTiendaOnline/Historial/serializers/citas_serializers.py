import re
from datetime import timezone

from django.core.exceptions import ValidationError
from rest_framework import serializers

from Historial.models import Citas, EstadoChoises, Usuarios, CamposChoises


class CitasSerializer(serializers.ModelSerializer):

    nie=serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    anotaciones = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=150)
    fecha=serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    campo = serializers.ChoiceField(
        choices=CamposChoises.choices,
        default=CamposChoises.MEDICINA_GENERAL,
        error_messages={"Camp_Error":"El campo introducido es invalido"}
    )
    estado = serializers.ChoiceField(
        choices=EstadoChoises.choices,
        default=EstadoChoises.PROCESS,
        error_messages={"Estade_Error": "Ese Estado es invalido"}
    )

    class Meta:
        model = Citas
        fields = ('nie',
                  'anotaciones',
                  'campo',
                  'fecha',
                  'estado',)

    def validate_nie(self, nie):
        if not Usuarios.objects.filter(nie=nie).exists():
            raise ValidationError("El NIE que intenta usar no esta registrado.")
        if re.search(r"^(?=.*\s)$", nie):
            raise serializers.ValidationError("No se permiten espacios en el NIE")
        if not re.search(r"^([XYZ])(\d{7})([A-Z]+)$", nie):
            raise serializers.ValidationError("El NIE no cumple con los parámetros")
        return nie

    def validate_fecha(self, fecha):
        if fecha < timezone.now().date():
            raise ValidationError("Fecha invalida")
        if Citas.objects.filter(fecha=fecha).exists():
            raise ValidationError("La Fecha ya esta reservada")
        return fecha

    def validate(self,attrs):
        return attrs

    def create(self,validated_data):
        cita = Citas.objects.create(
            nie=validated_data['nie'],
            anotaciones=validated_data['anotaciones'],
            fecha=validated_data['fecha'],
            campo=validated_data['campo'],
            estado=validated_data['estado']
        )
        cita.save()
        return cita