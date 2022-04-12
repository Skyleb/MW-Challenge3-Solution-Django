from django.contrib import admin
from .models import ContainerContent, ContactContainerContent, ContactInfo

admin.site.register(ContainerContent)
admin.site.register(ContactContainerContent)
admin.site.register(ContactInfo)