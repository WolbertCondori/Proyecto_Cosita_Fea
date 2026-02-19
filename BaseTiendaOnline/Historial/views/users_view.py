from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Historial.models import Usuarios, RolChoises
from Historial.serializers import UsersSerializer


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'success':True},status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = Usuarios.objects.all()
        data = [{
            'nombre':user.nombre,
            'email':user.email,
            'telefono':user.telefono,
            'nie':user.nie,
            'nc':user.nc,
            'fecha_nacimiento':user.fecha_nacimiento,
            'edad':user.edad,
            'rol':user.rol
        }
            for user in users]
        return Response({'data': data}, status=status.HTTP_200_OK)
