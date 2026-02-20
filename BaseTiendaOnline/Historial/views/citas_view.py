from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Historial.models import Citas
from Historial.serializers import CitasSerializer


class CitasView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CitasSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'success': True}, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,*args,**kwargs):
        user = request.query_params.get('user')
        citas = Citas.objects.all()
        if user:
            citas = Citas.objects.filter(nie__nie=user).all()
        data = [{
            'nie':cita.nie.nie,
            'fecha':str(cita.fecha.strftime('%Y-%m-%d %H:%M')),
            'anotaciones':cita.anotaciones,
            'campo':cita.campo,
            'estado':cita.get_estado_display(),
            'creado':cita.creado,
            'slug':cita.slug
        }
            for cita in citas]
        return Response({'data': data}, status=status.HTTP_200_OK)