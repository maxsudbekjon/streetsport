from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer
from apps.models import Order

from rest_framework.exceptions import ValidationError
from apps.models import Stadium

class StadiumListModelSerializer(ModelSerializer):
    class Meta:
        model=Stadium
        exclude=('created_at',)
class OrderModelSerializer(ModelSerializer):
    class Meta:
        model=Order
        exclude=('user','created_at')
    def validate(self, data):
        start_time=data['start_time']
        end_time=data['end_time']
        stadium=data['stadium'].id
        conflicting_orders=Order.objects.filter(stadium_id=stadium,start_time__lt=end_time ,end_time__gt=start_time)
        if conflicting_orders.exists():
            raise ValidationError('Bu vaqtda bron bor!')
        user = self.context['request'].user

        if not user.is_authenticated:
            raise ValidationError("Siz tizimga kirgan bo'lishingiz kerak.")

        if user.role != 'user':
            raise ValidationError("Faqat 'user' roli bo‘lgan foydalanuvchi stadion bron qila oladi.")

        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        stadium = validated_data['stadium']
        stadium.bron_count += 1
        stadium.save()
        return super().create(validated_data)
class BronStadiumTimeModelSerializer(ModelSerializer):
    start_time = DateTimeField(format="%Y-%m-%d %H:%M")
    end_time = DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model=Order
        fields=('stadium','start_time','end_time')