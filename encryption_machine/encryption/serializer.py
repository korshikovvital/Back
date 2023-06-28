from encryption.models import Encryption
from rest_framework import serializers


class EncryptionSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода результата шфирования"""
    class Meta:
        model = Encryption
        fields = (
            'id',
            'text',
            'algorithm',
            'key',
            'is_encryption',
        )
    
    def to_representation(self, instance):
        obj = super().to_representation(instance)
        obj_1 = Encryption.objects.get(id=obj['id'])
        encrypted_text = obj_1.get_algorithm()
        return {'encrypted_text': encrypted_text}
    