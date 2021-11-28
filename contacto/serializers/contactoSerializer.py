from django.db.models import fields
from rest_framework import serializers
from contacto.models import Contacto

class contactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "_id": str(instance._id),
            "nombre": instance.nombre,
            "email": instance.email,
            "telefono": instance.telefono,
            "inquietudes": instance.inquietudes,
            "comentario": instance.comentario,
            "sol_activa": instance.sol_activa, 
        }
        