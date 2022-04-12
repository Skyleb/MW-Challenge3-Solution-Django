# views.py

#from django.shortcuts import render
from rest_framework import viewsets, mixins

from .serializers import ContainerContentSerializer, ContactContainerContentSerializer, ContactInfoSerializer
from .models import ContainerContent, ContactContainerContent, ContactInfo

class ContainerContentViewSet(viewsets.ModelViewSet):
  queryset = ContainerContent.objects.all().order_by('id')
  serializer_class = ContainerContentSerializer

class ContactContainerContentViewSet(viewsets.ModelViewSet):
  queryset = ContactContainerContent.objects.all().order_by('id')
  serializer_class = ContactContainerContentSerializer

# class ContactInfoViewSet(viewsets.ModelViewSet):
#   queryset = ContactInfo.objects.all().order_by('id')
#   serializer_class = ContactInfoSerializer

class ContactInfoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  queryset = ContactInfo.objects.all().order_by('id')
  serializer_class = ContactInfoSerializer