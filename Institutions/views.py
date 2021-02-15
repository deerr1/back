from django.shortcuts import render
from rest_framework import generics, views
from django_filters import rest_framework as filters

from . import serializers, models
# Create your views here.




class WebsiteFilter(filters.FilterSet):
    
    subject = filters.CharFilter(field_name='points__subject__subject')
    form = filters.NumberFilter(field_name = 'form')
    # form = filters.ModelMultipleChoiceFilter(queryset=models.InfoInstitutions.objects.all())
    # qualification = filters.ModelMultipleChoiceFilter(queryset=models.InfoInstitutions.objects.all())
    # points__subject__subject = filters.ModelMultipleChoiceFilter(queryset=models.InfoInstitutions.objects.all())

    class Meta:
        model = models.InfoInstitutions
        fields = ['id','alias','points__subject__subject','form','availability_of_paid','availability_of_budger','qualification']

class InfoInstitutions(generics.ListAPIView):
    queryset = models.InfoInstitutions.objects.all()
    serializer_class = serializers.InfoInstSerializer
    filter_class = WebsiteFilter
    filter_fields = ['id','form','availability_of_budger','availability_of_paid','qualification','alias','direction','points__subject__subject']
    filter_backends = [filters.DjangoFilterBackend]
    # search_fields = ['@number_of_paid',]