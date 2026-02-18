from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

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
