
# Функция шифрования
def cipher_encrypt(plain_text, key):
    encrypted = ""
    for i in plain_text:
        if i.isupper(): #проверить, является ли символ прописным
            i_index = ord(i) - ord('А')
            # сдвиг текущего символа на позицию key
            i_shifted = (i_index + key) % 32 + ord('А')
            i_new = chr(i_shifted)
            encrypted += i_new
        elif i.islower(): #проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            i_index = ord(i) - ord('а')
            i_shifted = (i_index + key) % 32 + ord('а')
            i_new = chr(i_shifted)
            encrypted += i_new
        elif i.isdigit():
            # если это число, сдвинуть его фактическое значение 
            i_new = (int(i) + key) % 10
            encrypted += str(i_new)
        elif ord(i) >= 32 and ord(i) <= 47:
            # если это число, сдвинуть его фактическое значение
            i_index = ord(i) - ord(' ')
            i_shifted = (i_index + key) % 15 + ord(' ')
            i_new = chr(i_shifted)
            encrypted += i_new
        else:
            raise Exception(f'Вы ввели недопустимый символ {i}')
            # если нет ни алфавита, ни числа, оставьте все как есть
    return encrypted


# Функция дешифрования
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('А')
            # sсдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - key) % 32 + ord('А')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('а')
            c_og_pos = (c_index - key) % 32 + ord('а')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # если это число, сдвиньте его фактическое значение 
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        elif ord(c) >= 32 and ord(c) <= 47:
            # если это число,4 сдвинуть его фактическое значение
            i_index = ord(c) - ord(' ')
            i_shifted = (i_index - key) % 15 + ord(' ')
            i_new = chr(i_shifted)
            decrypted += i_new
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            decrypted += c
    return decrypted

user_text = input('Введите любой текст на русском\n')
user_key = int(input('Введите любое число\n'))

# шифрование
print(cipher_encrypt(user_text, user_key))
# дешифрование
print(cipher_decrypt(user_text, user_key))