from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from .serializers import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)


def isActive(request):
    return(request.user.is_active)

def isAdmin(request):
    return(request.user.is_admin)

def isModerator(request):
    return(request.user.is_staff)

def isFarmer(request):
    return(request.user.is_farmer)


from .forms import *

###User#######################################################################
#CreateUser
@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
        #serializer.save()
    return Response(serializer.data)

#UpdateUser
#TODO change
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def userUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserBasicSerializer(instance=user, data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        #serializer.save()
    return Response(serializer.data)

#DeleteUser
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userDelete(request, pk):
    if isAdmin(request) or request.user.id == pk:
        user = User.objects.get(id=pk)
        user.delete()
        return Response()

#GetAllUsers
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userList(request):
    if isAdmin(request):
        users = User.objects.all()
        serializer = UserBasicSerializer(users, many=True)
        return Response(serializer.data)

#TODO changed
#GetOneUser
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def userDetail(request, pk):
    user = User.objects.get(id=pk)
    # print('******tady je pk:\n', pk)
    # print('tady je user email:\n', user.email)
    # print('tady je request.user:\n', request.user)
    # if request.user.id == pk or isAdmin(request):
    if 1:
        serializer = UserBasicSerializer(user, many=False)
        return Response(serializer.data)
    return Response()

###Crop#######################################################################
#CreateCrop
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cropCreate(request):
    serializer = CropSerializer(data=request, many=True)
    return Response(serializer.data)

#UpdateCrop
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cropUpdate(request, pk):
    crop = Crop.objects.get(id=pk)
    serializer = CropSerializer(instance=crop, data=request.data ,many=False)
    return Response(serializer.data)

#DeleteCrop
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cropDelete(request, pk):
    crop = Crop.objects.get(id=pk)
    if isAdmin(request) or request.user.id == crop.farmer.id:
        crop.delete()
    return Response()

#AllCrops
@api_view(['GET'])
def cropList(request):
    crops = Crop.objects.all()
    serializer = CropSerializer(crops, many=True)
    return Response(serializer.data)

#CropByType
@api_view(['GET'])
def cropByType(request, type):
    cropType = CropCatalog.objects.get(cropType=type)
    crops = cropType.cropsByType.all()
    serializer = CropSerializer(crops, many=True)
    return Response(serializer.data)

#CropByFarmer
@api_view(['GET'])
def cropByFarmer(request, pk):
    farmer = User.objects.get(id=pk)
    crops = farmer.cropsByFarmer.all()
    serializer = CropSerializer(crops, many=True)
    return Response(serializer.data)

#######################CropCatalog########################################
@api_view(['POST'])
def cropCatalogCreate(request):
    serializer = CropCatalogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#UpdateCrop
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cropCatalogUpdate(request, pk):
    crop = CropCatalog.objects.get(id=pk)
    serializer = CropCatalogSerializer(instance=crop, data=request.data ,many=False)
    return Response(serializer.data)

#DeleteCropFromCatalog
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cropCatalogDelete(request, pk):
    crop = CropCatalog.objects.get(id=pk)
    if isModerator(request):
        crop.delete()
    return Response()

#CropCatalogList
@api_view(['GET'])
def cropCatalogList(request):
    crops = CropCatalog.objects.all()
    serializer = CropCatalogSerializer(crops, many=True)
    return Response(serializer.data)

#CropCatalogByCategory
@api_view(['GET'])
def cropCatalogByCategory(request, type):
    crops = CropCatalog.objects.filter(category=type)
    serializer = CropCatalogSerializer(crops, many=True)
    return Response(serializer.data)


###Harvest#######################################################################
#CreateHarvest
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def harvestCreate(request):
    serializer = HarvestSerializer(data=request, many=True)
    return Response(serializer.data)

#UpdateHarvest
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def harvestUpdate(request, pk):
    crop = Harvest.objects.get(id=pk)
    serializer = HarvestSerializer(instance=crop, data=request.data ,many=False)
    return Response(serializer.data)


#DeleteHarvest: Must be Authenticated and owner of the Harvest event!
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def harvestDelete(request, pk):
    try:
        crop = Harvest.objects.get(id=pk)
    except:
        crop = None
    if crop is not None:
        if request.user == crop.farmer:
            crop.delete()
    return Response()

#HarvestByCategory: Anyone can VIEW Harvest
@api_view(['GET'])
def harvestByCategory(request):
    harvest = Harvest.objects.all()
    serializer = HarvestSerializer(harvest, many=True)
    return Response(serializer.data)

#HarvestByFarmer: Anyone can View Harvest
@api_view(['GET'])
def harvestByFarmer(request, name):
    harvest = Harvest.objects.filter(farmer = name)
    serializer = HarvestSerializer(harvest, many=True)
    return Response(serializer.data)

#HarvestList: Anyone can VIEW Harvest
@api_view(['GET'])
def harvestList(request):
    harvest = Harvest.objects.all()
    serializer = HarvestSerializer(harvest, many=True)
    return Response(serializer.data)

#HarvestUserList
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def harvestUserList(request, pk):
    
    harvest = HarvestUsers.objects.filter(user=pk)
    user = User.objects.get(id=pk)

    if request.user == user.email:
        serializer = HarvestUsersSerializer(harvest, many=True)    
        return Response(serializer.data)
    else:
        return Response()
###Order#######################################################################

#CreateOrder
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def orderCreate(request):
    serializer = OrderSerializer(data=request, many=True)
    return Response(serializer.data)

#UpdateOrder
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def orderUpdate(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data ,many=False)
    return Response(serializer.data)

# #DeleteOrder
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def orderDelete(request, pk):
#     order = Order.objects.get(id=pk)
#     order.delete()
#     return Response()

#GetUsersOrders
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userOrderList(request, pk):
    user = User.objects.get(id=pk)
    if str(request.user) == str(user.email):
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    return Response()

#GetFarmerOrders
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def farmerOrders(request, pk):
    farmerUser = User.objects.get(id=pk)
    if str(request.user) == str(farmerUser.email):
        crops = Crop.objects.filter(farmer=farmerUser)
        list = crops.values_list('id',flat=True)
        
        orders = OrderDetail.objects.filter(crop__in=list)
        #print('\n***************\n', list, '\n***************\n')

        serializer = OrderDetailSerializer(orders,many=True)
        return Response(serializer.data)
    return Response()
    #print('\n***************\n', cropType.cropsByType.all(), '\n***************\n')
    

#OrderList
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def orderList(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

# #OrderDisplay
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def orderDisplay(request, pk):
#     order = Order.objects.get(id=pk)
#     serializer = OrderSerializer(order, many=False)
#     return Response(serializer.data)

#OrderDetailList
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def orderDetailList(request, pk):
    order = OrderDetail.objects.filter(order=pk)
    #if str(order.user.email) == (request.user):
    serializer = OrderDetailSerializer(order, many=True)
    return Response(serializer.data)








@api_view(['GET'])
def getAllCrop(request):
    crops = Crop.objects.all()
    serializer = GetAllCropSerializer(crops, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getAllHarvests(request):
    harvests = Harvest.objects.all()
    serializer = HarvestSerializer(harvests, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getAllUserEvents(request, pk):
    events = HarvestUsers.objects.filter(user=pk)
    serializer = HarvestDataSerializer(events, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getAllMyOrders(request,pk):

    orderDetail = OrderDetail.objects.all()

    serializer = OrderWholeSerializer(orderDetail, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllUserOffers(request,pk):

    crops = Crop.objects.filter(farmer=pk)

    serializer = CropSerializer(crops, many=True)
    return Response(serializer.data)



#CreateSuggestion
@api_view(['POST'])
def suggestionCreate(request):
    serializer = SuggestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#DeleteSuggestion
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def suggestionDelete(request, pk):
    try:
        suggestion = Suggestion.objects.get(id=pk)
        suggestion.delete()
    except:
        pass
    return Response()

@api_view(['GET'])
def getAllSuggestions(request):
    suggestion = Suggestion.objects.all()

    serializer = SuggestionSerializer(suggestion, many=True)
    return Response(serializer.data)
