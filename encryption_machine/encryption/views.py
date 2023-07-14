# from django.shortcuts import render
from encryption.models import Encryption
from encryption.serializer import EncryptionSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class EncryptionViewSet(ModelViewSet):
    """Вьюсет для шифрования"""
    queryset = Encryption.objects.all()
    serializer_class = EncryptionSerializer
    # http_method_names = ["post"]
