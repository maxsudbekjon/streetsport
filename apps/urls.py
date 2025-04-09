from django.urls import path
from apps.views import StadiumCreateAPIView, RegisterCreateAPIView, LoginAPIView, MyStadiumListAPIView, \
    AddManagerUpdateAPIView, StadiumListAPIView, OrderCreateAPIView, payment, ManagerStadiumAPIView, \
    OwnerBronStadionAPIView, BronStadiumTimeAPIView, StadiumUpdateAPIView





"""----------------------------------    OWNER     -----------------------------------------"""
urlpatterns=[
    path('stadium/create',StadiumCreateAPIView.as_view()),
    path('owner/stadium/list',MyStadiumListAPIView.as_view()),
    path('stadium/add/manager/<int:id>',AddManagerUpdateAPIView.as_view()),
    path('owner/bron/stadium/list',OwnerBronStadionAPIView.as_view()),
    path('owner/stadium/update/<int:id>',StadiumUpdateAPIView.as_view()),
]




"""----------------------------------    LOGIN/REGISTEER     -----------------------------------------"""
urlpatterns+=[
    path('register',RegisterCreateAPIView.as_view()),
    path('login',LoginAPIView.as_view())
]




"""----------------------------------    USER     -----------------------------------------"""
urlpatterns+=[
    path('stadium/list',StadiumListAPIView.as_view()),
    path('order/create',OrderCreateAPIView.as_view()),
    path('bron/stadium/time/list',BronStadiumTimeAPIView.as_view()),
]





"""----------------------------------    MANAGER     -----------------------------------------"""
urlpatterns+=[
    path('manager/payment/<int:id>',payment),
    path('manager/order/list',ManagerStadiumAPIView.as_view()),

]