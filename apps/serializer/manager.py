from enum import Enum

from rest_framework.fields import ChoiceField
from rest_framework.serializers import Serializer, ModelSerializer

from apps.models import Order


class StatusEnum(str, Enum):
    PAID = 'paid'
    DID_NOT_COME='did not come'
    THE_END='the end'

class PaymentSerializer(Serializer):
    status = ChoiceField(choices=[(tag.value, tag.name) for tag in StatusEnum])
class ManagerOrderModelSerializer(ModelSerializer):
    class Meta:
        model=Order
        exclude=('created_at',)