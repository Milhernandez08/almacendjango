from rest_framework import routers, serializers, viewsets
from apps.inventories.models import Inventory


class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('__all__')

