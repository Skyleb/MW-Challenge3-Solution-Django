# myapi/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'containercontent', views.ContainerContentViewSet)
router.register(r'contactcontainercontent', views.ContactContainerContentViewSet)
router.register(r'contactinfo', views.ContactInfoViewSet)


urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]