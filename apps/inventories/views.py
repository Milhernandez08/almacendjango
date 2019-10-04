from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.inventories.models import Inventory
from apps.inventories.serializers import InventorySerializers
 


class InventoriesList(APIView):
    def get(self, request, format=None):
        queryset = Inventory.objects.all()
        serializer = InventorySerializers(queryset, many=True)        
        return Response(serializer.data)        

class InventoriesDetail(APIView):
    def get_object(self, id):
        try:            
            return Inventory.objects.get(pk=id) 
        except Inventory.DoesNotExist: 
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = InventorySerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        rol = request.user.is_staff
        if rol == True:
            Inventory.objects.get(pk=id)
            return Response("Delete Success")
        else:
            return Response("No eres administrador")
    
    def put(self, request, id, format=None):        
        rol = request.user.is_staff
        example = self.get_object(id)
        if rol == True:
            if example != False:
                serializer = InventorySerializers(example, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    datas = serializer.data
                    return Response(datas)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response("No eres administrador")

