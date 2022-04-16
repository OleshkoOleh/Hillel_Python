s1 = 'Hillel_Python'
s2 = "Hillel_\tPython\n"
print(s1)
print(s2)

# Кодировки символов

# ASCII
# KOI -8R

# WIN - 1251 (for Windows)
# UTF8

code = 0x26bd               # unicode-table.com
print(chr(code))            #chr - функция обозначает/ Функция отображения символа из unicoda
print(chr(9917))
print('\u26bd')             # обозначает UNICODE \u - нижний регистр - 2 bytes \U - верхний регистр - 4 bytes
print('\U0001f6a3')

print(ord('🚣'))            #ord - функция может отобразить код из символа. Функция вернет 10-ричный код
print(hex(ord('🚣')))       #hex(ord - функция обозначает вывод 16-ричный код


