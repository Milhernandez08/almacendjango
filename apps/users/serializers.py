from rest_framework import routers, serializers, viewsets
from apps.inventories.models import Inventory
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password','email','is_superuser','date_joined')

