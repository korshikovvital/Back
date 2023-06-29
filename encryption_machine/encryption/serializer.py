from encryption.models import Encryption
from users.models import User
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
            'user'
        )

    def validate_algorithm(self, value):
        if value not in ('aes', 'caesar', 'morse', 'qr', 'vigenere'):
            raise serializers.ValidationError("Шрифт содержит неправильное название")
        return value

    def create(self, validated_data):
        user = self.context.get('request').user
        if user.is_authenticated:
            encryption = Encryption.objects.create(user=user, **validated_data)
        else:
            encryption = Encryption.objects.create(**validated_data)
        return encryption
    
    def to_representation(self, instance):
        obj = super().to_representation(instance)
        obj_1 = Encryption.objects.get(id=obj['id'])
        encrypted_text = obj_1.get_algorithm()
        return {'encrypted_text': encrypted_text}
    