from pyexpat.errors import messages

from django.template.context_processors import request
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from apps.models import Order, Stadium
from apps.serializer import PaymentSerializer, StatusEnum, ManagerOrderModelSerializer


@extend_schema(request=PaymentSerializer)
@api_view(['POST'])
def payment(request, id):
    order=Order.objects.filter(id=id)
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.validated_data['status'] == 'paid':
            message = "✅ To‘lov qilingan"
        elif serializer.validated_data['status'] == 'the end':
            message = "⏱️ To'lov qilishi kutilmoqda"
        else:
            order.delete()
            message='❌ Bron bekor qilindi'

        return Response({
            'message': message
        }, status=HTTP_200_OK)

    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class ManagerStadiumAPIView(APIView):
    def get(self,request):
        if request.user.role=='manager':
            manager_id=request.user.id
            stadiums=Stadium.objects.filter(manager=manager_id)
            orders=Order.objects.filter(stadium__in=stadiums)
            serializer=ManagerOrderModelSerializer(orders,many=True)
            return Response(serializer.data)
        raise ValidationError('Siz manager emassiz!')