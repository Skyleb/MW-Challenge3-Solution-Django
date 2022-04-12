# serializers.py

from rest_framework import serializers

from .models import ContainerContent, ContactContainerContent, ContactInfo

class ContainerContentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ContainerContent
    fields = ('id', 'iconPath', 'title', 'content')

class ContactContainerContentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ContactContainerContent
    fields = ('id', 'title', 'content')

class ContactInfoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ContactInfo
    fields = ('id', 'first_name', 'last_name', 'title', 'email', 'message')