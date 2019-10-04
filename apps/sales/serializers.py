from rest_framework import routers, serializers, viewsets
from apps.sales.models import Sale


class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('__all__')

