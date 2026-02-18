import re
from datetime import timezone

from django.core.exceptions import ValidationError

from Historial import serializers
from Historial.models import Citas, EstadoChoises, Usuarios


class CitasSerializer(serializers.ModelSerializer):

    nie=serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    fecha=serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    estado = serializers.ChoiceField(
        choices=EstadoChoises.choices,
        default=EstadoChoises.PACIENTE,
        error_messages={"Estade_Error": "Ese Estado es Invalido"}
    )

    class Meta:
        model = Citas
        fields = ('nie',
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

    def validate(self,attrs):
        return attrs

    def create(self,validated_data):
        cita =