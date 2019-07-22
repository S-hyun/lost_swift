from .models import *

from rest_framework import serializers
from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartegory
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'