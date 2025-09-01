from jsonschema.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Stadium, Order
from apps.serializer import StadiumListModelSerializer, OrderModelSerializer, BronStadiumTimeModelSerializer


class StadiumListAPIView(APIView):
    def get(self,request):
        user=request.user.role
        if user=='user':
            stadium=Stadium.objects.all()
            serializer=StadiumListModelSerializer(stadium,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message':"User role dagi foydalanuvchigini barcha stadionlarni ro'yxatini ko'ra oladi"})
class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
class BronStadiumTimeAPIView(APIView):
    def get(self,request):
        user_id=request.user
        user = request.user.id #12
        Stadium.objects.filter()
        if user == 'user':
            order=Order.objects.all()
            serializer=BronStadiumTimeModelSerializer(order,many=True)
            return Response(serializer.data)
        else:
            raise ValidationError('Siz user role da emassiz')