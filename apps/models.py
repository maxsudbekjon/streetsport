from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices, CharField, Model, ForeignKey, CASCADE, IntegerField, SET_NULL, ImageField, \
    ManyToManyField, DateField, BigIntegerField, DateTimeField
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class User(AbstractUser):
    class ROLE(TextChoices):
        ADMIN='admin','Admin'
        MANAGER='manager','Manager'
        OWNER='owner','Owner'
        USER='user','User'
    role=CharField(max_length=10,choices=ROLE.choices,default=ROLE.USER)
    phone_number=BigIntegerField(unique=True,blank=True,null=True)
    def __str__(self):
        return self.username


class Stadium(Model):
    class STATUS(TextChoices):
        NEW='new','New'
        AVERAGE='average','Average'
        OLD='old','Old'
    title=CharField(max_length=255)
    owner=ForeignKey('apps.User',CASCADE,related_name='stadiums')
    stadium_status=CharField(max_length=10,choices=STATUS.choices,default=STATUS.NEW)
    width=IntegerField()
    height=IntegerField()
    manager=ForeignKey('apps.User',SET_NULL,blank=True,null=True)
    address=CharField(max_length=255)
    created_at=DateField(auto_now_add=True)
    bron_count=IntegerField(default=0)
    def __str__(self):
        return self.title
class StadiumImage(Model):
    stadium=ForeignKey('apps.Stadium',CASCADE,related_name='images')
    image=ImageField(upload_to='stadium_image')


class Order(Model):
    user=ForeignKey('apps.User',CASCADE)
    stadium=ForeignKey('apps.Stadium',CASCADE)
    start_time=DateTimeField()
    end_time=DateTimeField()
    created_at=DateField(auto_now_add=True)
