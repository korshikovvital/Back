def vigenere_codec(text: str, key: str, codec: int = 1, lang: str = 'nd'):
    '''
    Код Виженера.
    Для повышения устойчивости все слова переводятся в верхний регистр,
    Цифры и знаки не шифруются. Исходный текст желательно вводить без пробелов.
    В фунцию передается текст для шифровки/дешифровки,
    ключ шифрования,
    опционально: параметр codec для определения
    направления шифрования (1 - шифровка(умолч.)/ -1 - дешифровка),
    параметр lang - язык текста и ключа.
    '''

    result = ''

    # Словарь алфавитов.
    # название_языка : [код_первого_символа, длина_алфавита]
    lang_dict = {'en': [64, 26],
                 'ru': [1039, 32]}

    # Определяем язык ключа. Язык по умолчанию nd (not defined)
    if lang == 'nd':
        for letter in key:
            for lang_test, [lang_start, lang_len] in lang_dict.items():
                if 0 <= (ord(letter) - lang_start) <= lang_len:
                    lang = lang_test
                    break
            if lang != 'nd':
                break

    # Если язык неизвестен, то текст возвращается в исходном виде.
    if lang not in lang_dict.keys():
        return (text)

    # код первой буквы алфавита
    zero_letter = lang_dict[lang][0]
    # длина алфавита
    alphabet_length = lang_dict[lang][1]

    # Шифрование предполагает сдвиг кода буквы на число,
    # соответствующее коду соответствующей буквы ключа.
    i = 0
    for letter in text.upper():
        if zero_letter < ord(letter) < zero_letter + alphabet_length:
            result += chr((ord(key[i]) * codec - 1 + ord(letter)
                           - 2 * zero_letter) % alphabet_length + zero_letter)
            i = i + 1 if i < len(key) - 1 else 0
        else:
            result += letter
    return result


def encode(text: str, key: str, codec: int = 1, lang: str = 'nd'):
    return vigenere_codec(text, key, 1, lang)


def decode(text: str, key: str, codec: int = 1, lang: str = 'nd'):
    return vigenere_codec(text, key, -1, lang)
