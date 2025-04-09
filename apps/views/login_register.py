from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import User
from apps.serializer import RegisterModelSerializer, LoginSerializer


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Muvaffaqiyatli login!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Noto\'g\'ri login yoki parol'}, status=status.HTTP_401_UNAUTHORIZED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)