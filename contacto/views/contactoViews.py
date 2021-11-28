from contacto.models import Contacto
from contacto.serializers import contactoSerializer
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from bson.objectid import ObjectId
from django.core import serializers
import json

class contactoCreate(generics.ListCreateAPIView):
    serializer_class = contactoSerializer
    queryset = Contacto.objects.all()

class contactoDetails(generics.RetrieveAPIView):
    serializer_class = contactoSerializer
    def get(self, request, *args, **kwargs):
        """
        se crea un objecto de tipo objectid para filtrar por la llave en mongo atlas,
        luego se trae el objeto y se serializa para enviar luego los campos necesarios
        """
        contacto = get_object_or_404(Contacto, _id=ObjectId(kwargs["_id"]))
        serialized_obj = serializers.serialize('json', (contacto,))
        struct = json.loads(serialized_obj)
        return Response(struct[0]["fields"], status=status.HTTP_200_OK)

class filterByEmail(generics.ListAPIView):
    serializer_class = contactoSerializer
    def get_queryset(self):
        queryset = Contacto.objects.filter(email=self.kwargs["email"])
        return queryset
