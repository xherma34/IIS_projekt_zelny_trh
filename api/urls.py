from django.contrib import admin
from django.urls import path

from .views import *
from . import views

from django.views.generic import TemplateView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path('', views.getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # #Login
    # path('', homePage),
    # path('login1/', userLogin),
    # path('register1/', userRegister),
    # path('hovno/', hovno),

    #User
    path('userList/', userList),
    path('userDetail/<str:pk>', userDetail),
    path('userCreate/', userCreate),
    path('userDelete/<str:pk>', userDelete),

    path('userOrderList/<str:pk>', userOrderList),

    #Crops
    path('cropList/', cropList),
    path('cropByType/<str:type>', cropByType),
    path('cropByFarmer/<str:pk>', cropByFarmer),
    

    #Catalog
    path('cropCatalogList/', cropCatalogList),
    path('cropCatalogByCategory/<str:type>', cropCatalogByCategory),

    #Harvest
    path('harvestList/', harvestList),
    path('harvestDelete/<str:pk>', harvestDelete),
    path('harvestUserList/<str:pk>', harvestUserList),
    path('harvestByFarmer/<str:name>', harvestByFarmer),

    #Order
    #path('orderList/', orderList),
    path('orderDetailList/<str:pk>', orderDetailList),
    path('farmerOrders/<str:pk>', farmerOrders),
    #path('orderDisplay/<str:pk>', orderDisplay),
    
]
