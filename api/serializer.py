from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Meniu.models import Menu
from Order.models import Order

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class CodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = ['fel1', 'fel2', 'desert']

# class ratingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['rating']
        

    