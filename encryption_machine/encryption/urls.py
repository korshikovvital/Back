from . import views
from django.urls import include, path
from .views import EncryptionViewSet
from rest_framework.routers import DefaultRouter

app_name = 'encryption'

router = DefaultRouter()

router.register('encryption', EncryptionViewSet, basename='encryption')


urlpatterns = [
    path('', include(router.urls)),
]
