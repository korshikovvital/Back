# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from encryption.models import Encryption
from encryption.serializer import EncryptionSerializer


class EncryptionViewSet(ModelViewSet):
    """Вьюсет для шифрования"""
    queryset = Encryption.objects.all()
    serializer_class = EncryptionSerializer
    http_method_names = ["post"]
