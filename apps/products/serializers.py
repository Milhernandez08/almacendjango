from rest_framework import routers, serializers, viewsets
from apps.products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

