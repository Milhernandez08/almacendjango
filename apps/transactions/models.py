from django.db import models
from apps.inventories.models import Inventory


class Transaction(models.Model):
    inventory    = models.ForeignKey( Inventory, related_name='transactions', on_delete=models.CASCADE )
    dates        = models.DateTimeField( default = False )
    types        = models.IntegerField( blank=False )
    quantity     = models.IntegerField( blank=False )
    description  = models.TextField( blank=False )

    class Meta:
        db_table = "transactions"
