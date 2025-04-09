from django.contrib.auth import get_user_model
from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer



from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.models import Stadium, Order


class StadiumCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        exclude = ('created_at', 'owner','manager')

    def validate(self, data):
        user = self.context['request'].user

        if not user.is_authenticated:
            raise ValidationError("Siz tizimga kirgan bo'lishingiz kerak.")

        if user.role != 'owner':
            raise ValidationError("Faqat 'owner' roli bo‘lgan foydalanuvchi stadion qo‘sha oladi.")

        manager = data.get('manager')
        if manager and manager.role != 'manager':
            raise ValidationError("Faqat 'manager' roli bo‘lgan foydalanuvchi menejer bo‘la oladi.")

        return data

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

class MyStadiumListModelSerializer(ModelSerializer):
    class Meta:
        model=Stadium
        exclude='created_at','owner'

class AddManagerStadiumSerializer(ModelSerializer):
    class Meta:
        model=Stadium
        fields=('manager',)
    def validate(self, data):
        user = self.context['request'].user

        if not user.is_authenticated:
            raise ValidationError("Siz tizimga kirgan bo'lishingiz kerak.")
        manager = data.get('manager')
        if manager and manager.role != 'manager':
            raise ValidationError("Faqat 'manager' roli bo‘lgan foydalanuvchi menejer bo‘la oladi.")

        return data
User = get_user_model()

class UserShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone_number')
class OrderOwnerStadiumModelSerializer(ModelSerializer):
    user = UserShortInfoSerializer()
    start_time = DateTimeField(format="%Y-%m-%d %H:%M")
    end_time = DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model=Order
        exclude=('created_at','id')
