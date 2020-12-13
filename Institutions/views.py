from django.shortcuts import render
from rest_framework import generics, views

from . import serializers, models
# Create your views here.

class InfoInstitutions(generics.ListAPIView):
    queryset = models.InfoInstitutions.objects.all()
    serializer_class = serializers.InfoInstSerializer
    filter_fields = ['id','form','qualification','alias','direction']