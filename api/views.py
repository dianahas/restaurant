from django.shortcuts import render

# Create your views here.
from Order.models import Order
from Meniu.models import Menu
from .serializer import *
from django.http import Http404
import datetime 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from restaurant.utils import *

class MenuList(APIView):
   
    def get(self, request, format=None):
        today = datetime.date.today()
        menus = Menu.objects.all().filter(datta=today)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class MenuDetail(APIView):

    def get_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        meniu = self.get_object(pk)
        serializer = MenuSerializer(meniu)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        meniu = self.get_object(pk)
        serializer = MenuSerializer(meniu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        meniu = self.get_object(pk)
        meniu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):
    
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        #import ipdb; ipdb.set_trace()
        orders = Order.objects.all()
        data = request.data
        name = data["name"]
        adress = data["adress"]
        if validateString(name) == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if validateString(adress) == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        idMeniu = data["id_menu"]
        try:
            meniu = Menu.objects.get(pk=idMeniu)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        theRating = data["rating"]
        theStatus = data["status"]
        if theStatus != 0 or theRating != 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            subject = "Order confirmation"
            mail = data["email"]
            menu_code = str(data["id_menu"]) + "-"
            orderr = Order.objects.last()
            menu_code += str(orderr.pk)
            send_mail(subject, menu_code, "restaurantarchers@gmail.com", [mail])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


class orderByCode(APIView):
    
    def post(self, request, format=None):
        #import ipdb; ipdb.set_trace()
        receivedData = request.data["code"]
        if validateCode(receivedData) == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        tup = validateCode(receivedData)
        meniu = Menu.objects.get(pk=tup[0])
        comanda = Order.objects.get(pk=tup[1])
        serializer = CodeSerializer(meniu)
        
        dateResponse = serializer.data
        dateResponse["status"] = comanda.status
        return Response(dateResponse, status=status.HTTP_200_OK)

class updateRating(APIView):

    def post(self, request, format=None):
        data = request.data["code"]
        if validateCode(data) == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        tup = validateCode(data)
        codOrder = tup[1]
        receivedRequest = request.data["rating"]
        selectedOrder = Order.objects.get(pk=codOrder)
        if selectedOrder.status == 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)   
        try:
            theRating = float(receivedRequest)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        if theRating<=0 or theRating >5 : 
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        selectedOrder.rating = request.data["rating"]
        selectedOrder.status = 2
        selectedOrder.save()

        return Response(status=status.HTTP_201_CREATED)
    
    