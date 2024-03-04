encryption_or_decryption = input('Шифрование или дешифрование?')
language = input('Русский или английский?')
k = int(input('Шаг сдвига (со сдвигом вправо)?'))
alp_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alp_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alp_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp_en = 'abcdefghijklmnopqrstuvwxyz'
s = input('Введите строку')
s1 = ''
if encryption_or_decryption.lower() == 'шифрование':
    if language.lower() == 'русский':
        for c in s:
            if c in alp_RU:
                s1 += alp_RU[(alp_RU.find(c) + k) % 32]
            elif c in alp_ru:
                s1 += alp_ru[(alp_ru.find(c) + k) % 32]
            else:
                s1 += c
    elif language.lower() == 'английский':
        for c in s:
            if c in alp_EN:
                s1 += alp_EN[(alp_EN.find(c) + k) % 26]
            elif c in alp_en:
                s1 += alp_en[(alp_en.find(c) + k) % 26]
            else:
                s1 += c
if encryption_or_decryption.lower() == 'дешифрование':
    if language.lower() == 'русский':
        for c in s:
            if c in alp_RU:
                s1 += alp_RU[(alp_RU.find(c) - k) % 32]
            elif c in alp_ru:
                s1 += alp_ru[(alp_ru.find(c) - k) % 32]
            else:
                s1 += c
    elif language.lower() == 'английский':
        for c in s:
            if c in alp_EN:
                s1 += alp_EN[(alp_EN.find(c) - k) % 26]
            elif c in alp_en:
                s1 += alp_en[(alp_en.find(c) - k) % 26]
            else:
                s1 += c
print(s1)