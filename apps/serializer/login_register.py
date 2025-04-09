from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer, ValidationError, Serializer

from apps.models import Stadium, User

class RegisterModelSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=('username','role','phone_number','password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
class LoginSerializer(Serializer):
    username=CharField(max_length=255)
    password=CharField(max_length=255)