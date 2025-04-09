from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Stadium, Order
from apps.serializer import StadiumCreateModelSerializer, MyStadiumListModelSerializer, AddManagerStadiumSerializer, \
    OrderOwnerStadiumModelSerializer


class StadiumCreateAPIView(CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumCreateModelSerializer
class MyStadiumListAPIView(APIView):
    def get(self,request):
        owner_id=request.user.id
        stadiums=Stadium.objects.filter(owner_id=owner_id)
        serializer=MyStadiumListModelSerializer(stadiums,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class AddManagerUpdateAPIView(UpdateAPIView):
    queryset = Stadium
    serializer_class = AddManagerStadiumSerializer
    lookup_field = 'id'
class OwnerBronStadionAPIView(APIView):
    def get(self,request):
        owner_id=request.user.id
        stadium=Stadium.objects.filter(owner_id=owner_id)
        order=Order.objects.filter(stadium__in=stadium)
        serializer=OrderOwnerStadiumModelSerializer(order,many=True)
        return Response(serializer.data)
class StadiumUpdateAPIView(UpdateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = MyStadiumListModelSerializer
    lookup_field = 'id'