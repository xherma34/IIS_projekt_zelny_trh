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
    path('userDetail/<int:pk>', userDetail),
    path('userCreate/', userCreate),
    path('userDelete/<int:pk>', userDelete),    #TODO changed
    path('userUpdate/<int:pk>', userUpdate),    #TODO changed

    path('userOrderList/<str:pk>', userOrderList),

    #Crops
    path('cropList/', cropList),
    path('cropByType/<str:type>', cropByType),
    path('cropByFarmer/<str:pk>', cropByFarmer),
    path('getAllCrop/', getAllCrop),
    

    #Catalog
    path('cropCatalogCreate/', cropCatalogCreate),
    path('cropCatalogList/', cropCatalogList),
    path('cropCatalogByCategory/<str:type>', cropCatalogByCategory),

    #Harvest
    path('harvestList/', harvestList),
    path('harvestDelete/<str:pk>', harvestDelete),
    path('harvestUserList/<str:pk>', harvestUserList),
    path('harvestByFarmer/<str:name>', harvestByFarmer),
    path('getAllUserEvents/<str:pk>', getAllUserEvents),
    path('getAllHarvests/', getAllHarvests),

    #Order
    path('orderList/', orderList),
    path('orderDetailList/<str:pk>', orderDetailList),
    path('farmerOrders/<str:pk>', farmerOrders),
    #path('orderDisplay/<str:pk>', orderDisplay),
    path('getAllMyOrders/<str:pk>', getAllMyOrders),
    
    #Offer
    path('getAllUserOffers/<str:pk>', getAllUserOffers),

    #Suggestions
    path('getAllSuggestions/', getAllSuggestions),
    path('suggestionCreate/', suggestionCreate),
    path('suggestionDelete/<str:pk>', suggestionDelete),
]
