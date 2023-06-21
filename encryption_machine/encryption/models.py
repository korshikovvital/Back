from django.db import models

from users.models import User

from .encryption_algorithms import aes, morse_code


class Encryption(models.Model):
    """Модель шифрования."""
    user = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='encryptions')
    text = models.TextField(max_length=2000)
    encryption_algorithm = models.CharField(max_length=100)
    key = models.CharField(max_length=100, null=True)
    is_encryption = models.BooleanField()  # True - шифруем, False - дешифруем

    class Meta:
        verbose_name = 'Шифрование'
        verbose_name_plural = 'Шифрования'

    def encrypt_aes(text, key):
        return aes.encrypt(text, key)

    def decrypt_aes(text, key):
        return aes.decrypt(text, key)

    def encryption_mixin_caesar(text, key):
        final_string = ""
        for symbol in text:
            if symbol.isupper():
                symbol_index = ord(symbol) + ord('А')
                if self.is_encryption:
                # sсдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
                    symbol_position = (symbol_index + key) % 32 + ord('А')
                else:
                    symbol_position = (symbol_index - key) % 32 + ord('А')
                symbol_new = chr(symbol_position)
                final_string += symbol_new
            elif symbol.islower():
                symbol_index = ord(symbol) - ord('а')
                if self.is_encryption:
                    symbol_position = (symbol_index + key) % 32 + ord('а')
                else:
                    symbol_position = (symbol_index - key) % 32 + ord('а')
                symbol_new = chr(symbol_position)
                final_string += symbol_new
            elif symbol.isdigit():
                # если это число, сдвиньте его фактическое значение
                if self.is_encryption:
                    symbol_index = (int(symbol) + key) % 10
                else:
                    symbol_index = (int(symbol) - key) % 10
                final_string += str(symbol_index)
            elif ord(symbol) >= 32 and ord(symbol) <= 47:
                # если это число,4 сдвинуть его фактическое значение
                symbol_index = ord(symbol) - ord(' ')
                if self.is_encryption:
                    symbol_position = (symbol_index + key) % 15 + ord(' ')
                else:
                    symbol_position = (symbol_index - key) % 15 + ord(' ')
                symbol_new = chr(symbol_position)
                final_string += symbol_new
            else:
                # если нет ни алфавита, ни числа, оставьте все как есть
                final_string += symbol
        return final_string

    def encrypt_dsa(text, key):
        pass

    def decrypt_dsa(text, key):
        pass

    def encrypt_morse(text):
        return morse_code.encode(text)

    def decrypt_morse(text):
        return morse_code.decode(text)

    def encrypt_qr(text):
        pass

    def decrypt_qr(text):
        pass

    def encrypt_vigenere(text, key):
        pass

    def decrypt_vigenere(text, key):
        pass