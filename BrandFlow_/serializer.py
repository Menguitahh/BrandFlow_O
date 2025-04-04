from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('iduser', 'username', "password", "email",'phone', 'addres')
        fields = '__all__'


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
        

# class CampaignSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Campaingn
#         fields = '__all__'

# class CampaignUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CampaignUser
#         fields = '__all__'
        

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'
        


