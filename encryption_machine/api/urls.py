from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (EncryptionListViewSet, reset_password,
                    reset_password_confirm, reset_password_question)

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register(
    'users/me/encryptions', EncryptionListViewSet, basename='encryption-list')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('users/reset_password/', reset_password, name='reset_password'),
    path(
        'users/reset_password_question/',
        reset_password_question,
        name='reset_password_question'
    ),
    path(
        'users/reset_password_confirm/',
        reset_password_confirm,
        name='reset_password_confirm'
    ),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('encryption.urls'))
]
