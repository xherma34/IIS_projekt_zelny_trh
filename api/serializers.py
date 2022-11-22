from rest_framework import serializers
from .models import *






class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName','lastName', 'email', 'id', 'dateOfBirth', 'phone']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'


class GetAllCropSerializer(serializers.ModelSerializer):
    
    farmer = UserBasicSerializer()
    class Meta:
        model = Crop
        fields = '__all__'


class CropCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropCatalog
        fields = '__all__'

class HarvestSerializer(serializers.ModelSerializer):
    farmer = UserBasicSerializer()
    class Meta:
        model = Harvest
        fields = '__all__'

class HarvestUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestUsers
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class FarmerOfHarvestSerializer(serializers.ModelSerializer):

    farmer = UserBasicSerializer()
    class Meta:
        model = Harvest
        fields='__all__'

class HarvestDataSerializer(serializers.ModelSerializer):

    harvest = FarmerOfHarvestSerializer()
    class Meta:
        model = HarvestUsers
        fields = '__all__'

# class CropOrderDetailSerializer(serializers.ModelSerializer):
#     farmer = UserBasicSerializer()
#     class Meta:
#         model = Crop
#         fields = '__all__'


class CropOrderDetailSerializer(serializers.ModelSerializer):
    farmer = UserBasicSerializer()
    class Meta:
        model = Crop
        fields = '__all__'


class TestOrderSerializer(serializers.ModelSerializer):

    order = OrderSerializer()
    crop = CropOrderDetailSerializer(many=False)
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderWholeSerializer(serializers.ModelSerializer):

    order = OrderSerializer()
    crop = CropOrderDetailSerializer(many=False)
    class Meta:
        model = OrderDetail
        fields = '__all__'

class SuggestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suggestion
        fields = '__all__'