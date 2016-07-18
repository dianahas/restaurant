from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Meniu.models import Menu
from Order.models import Order

#Here are declared the serializer classes. 

#menu serializer
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu

#order serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

#custom menu serializer
class CodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = ['fel1', 'fel2', 'desert','datta']



    