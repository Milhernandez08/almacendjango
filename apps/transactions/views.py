from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transactions.models import Transaction
from apps.transactions.serializers import TransactionSerializers


class TransactionsList(APIView):
    def get(self, request, format=None):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializers(queryset, many=True)        
        return Response(serializer.data)

class TransactionsDetail(APIView):
    def get_object(self, id):
        try:            
            return Transaction.objects.get(pk=id) 
        except Inventory.DoesNotExist: 
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = TransactionSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
