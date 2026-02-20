from django.core.serializers import serialize
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
        u = request.query_params.get('user')
        data = [{
            'nombre': user.nombre,
            'email': user.email,
            'telefono': user.telefono,
            'nie': user.nie,
            'nc': user.nc,
            'fecha_nacimiento': user.fecha_nacimiento,
            'edad': user.edad,
            'rol': user.rol,
            'img': request.build_absolute_uri(user.img.url),
        }
            for user in users]
        if u:
            usuario = Usuarios.objects.filter(nie=u).first()
            data={
                'nombre': usuario.nombre,
                'email': usuario.email,
                'telefono': usuario.telefono,
                'nie': usuario.nie,
                'nc': usuario.nc,
                'fecha_nacimiento': usuario.fecha_nacimiento,
                'edad': usuario.edad,
                'rol': usuario.rol,
                'img': request.build_absolute_uri(usuario.img.url),
            }
        return Response({'data': data}, status=status.HTTP_200_OK)

    def patch(self, request):
        user = Usuarios.objects.filter(nie=request.data["nie"]).first()
        serializer = UsersSerializer(user, img=request.data["img"],partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'success':True},status=status.HTTP_206_PARTIAL_CONTENT)
            except:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
