from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sales.models import Sale
from apps.sales.serializers import SaleSerializers
from apps.inventories.models import Inventory
from apps.sales.operaciones import Operaciones
from apps.inventories.serializers import InventorySerializers
from apps.transactions.models import Transaction
from apps.products.models import Product
from apps.products.serializers import ProductSerializers


class SalesList(APIView):    
    def get(self, request, format=None):
        queryset = Sale.objects.all()
        serializer = SaleSerializers(queryset, many=True)        
        return Response(serializer.data)


    def post(self, request, format=None):        
        #saleInventory = SaleSerializers(data = request.data)

        print("Request ", request.data)
        productId = int(request.data['product'])
        print("type value", type(productId))
        
        SALES = request.data

        searchIdProduct = Inventory.objects.get(product=int(SALES['product'])) 
        serializerInventory = InventorySerializers(searchIdProduct)                     
        INVENTORY = serializerInventory.data

        print("Vlues inventory", INVENTORY)
        ##########  POST FOR TRANSACTIONS #############                             
        op = Operaciones(INVENTORY, SALES)
        print(op.total())        
        newSale = Sale.objects.create(
            user_id     = request.user.id,
            product_id  = request.data['product'],
            quantity    = request.data['quantity'],
            discount    = SALES['discount'],
            total       = op.total(),
            dates       = timezone.now(),
            payment     = SALES['payment'],
            status      = SALES['status'],            
        )        
        newSale.save()
        ##########  UPDATE FOR PRODUCTS #############
        Inventory.objects.filter(pk=int(SALES['product'])).update(
            quantity = op.residuo()
        )        
        
        ##########  POST FOR TRANSACTIONS #############
        inventoryIdProductSale = INVENTORY['id']
        
        idProduct = int(request.data['product'])
        searchIdProductInProducts = Product.objects.get(pk=idProduct) 
        serializerProduct= ProductSerializers(searchIdProductInProducts)                     
        PRODUCT = serializerProduct.data

        Transaction.objects.create(
            inventory_id    = inventoryIdProductSale,
            dates           = timezone.now(),
            types           = 2,
            quantity        = request.data['quantity'],
            description     = "Se vendio " + request.data['quantity'] + " "+PRODUCT['name']
        )                    
        return Response("Success")

class SalesDetail(APIView):
    def get_object(self, id):
        try:            
            return Sale.objects.get(pk=id) 
        except Inventory.DoesNotExist: 
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, id, format=None):        
        rol = request.user.is_superuser
        idSale = self.get_object(id)
        
        if rol == True:                        
            searchIdSale = Sale.objects.get(pk=id) 
            serializerSale = SaleSerializers(searchIdSale)                     
            SALE = serializerSale.data            
            ##########  UPDATE FOR status SALE #############
            Sale.objects.filter(pk=id).update(
                status = request.data['status']
            )

            ##########  POST FOR TRANSACTIONS ############# 
            searchIdProduct = Inventory.objects.get(product=int(SALE['product'])) 
            serializerInventory = InventorySerializers(searchIdProduct)                     
            INVENTORY = serializerInventory.data
                                        
            op = Operaciones(INVENTORY, SALE)            
            Inventory.objects.filter(pk=int(SALE['product'])).update(
                quantity = op.residuo()
            )

            ##########  POST FOR TRANSACTIONS #############
            inventoryIdProductSale = INVENTORY['id']
            print("ID inv sale: ", inventoryIdProductSale)
            idProduct = int(request.data['product'])
            searchIdProductInProducts = Product.objects.get(pk=idProduct) 
            serializerProduct= ProductSerializers(searchIdProductInProducts)                     
            PRODUCT = serializerProduct.data

            Transaction.objects.create(
                inventory_id    = inventoryIdProductSale,
                dates           = timezone.now(),
                types           = 2,
                quantity        = op.residuo(),
                description     = "Se cancelo la venta del producto " + PRODUCT['name']
            )                                
        return Response("Success")
