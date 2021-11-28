from djongo import models

class Contacto(models.Model):
    inquietudes = (
        (0, "Producto"),
        (1, "Servicio de entrega"),
        (2, "Otro"),
    )
    _id = models.ObjectIdField(primary_key= True)
    nombre = models.CharField(max_length=50, null=True)
    telefono = models.IntegerField(null=True)
    email = models.EmailField(max_length=50, null=True)
    inquietudes = models.CharField(max_length=2, choices=inquietudes, null=True)
    comentario = models.TextField(max_length=2000, null=True)
    sol_activa = models.BooleanField(default=True, null=True)
