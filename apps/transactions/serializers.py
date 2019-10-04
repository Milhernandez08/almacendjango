from rest_framework import routers, serializers, viewsets
from apps.transactions.models import Transaction


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')

