from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from datetime import date
import os


class Product(models.Model):        
    code        = models.IntegerField( blank=False )
    name        = models.CharField( max_length=50, blank=True )
    description = models.TextField( blank=False)    
    
    #SUBIR LA IMAGEN
    def _generar_ruta_imagen(instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, se usa el nombre de la clase y la fecha actual.
        directorio_clase = instance.__class__.__name__
        ruta = os.path.join('images', directorio_clase,
            date.today().strftime("%Y/%m"))

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(uuid4().hex, extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)

    image       = models.ImageField(upload_to=_generar_ruta_imagen)
        
    class Meta:
        db_table = "products"

 


