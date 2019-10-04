from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

class Inventory(models.Model):
    product     = models.ForeignKey( Product, verbose_name='inventories', on_delete=models.CASCADE ) 
    user        = models.ForeignKey( User, verbose_name='inventories', on_delete=models.CASCADE )
    quantity    = models.IntegerField( null=False )
    price       = models.DecimalField( max_digits=10, decimal_places=2 )
    tax         = models.DecimalField( max_digits=5, decimal_places=2 )
    class Meta:
        db_table = "inventories"
 

