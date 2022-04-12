s1 = 'Hillel_Python'
s2 = "Hillel_Python"

# ASCII
# KOI -8R

# WIN - 1251 (for Windows)
# UTF8

code = 0x26bd
print(chr(code))
print(chr(9917))
print('\u26bd')             # обозначает UNICODE \u - нижний регистр - 2 bytes \U - верхний регистр - 4 bytes
print('\U0001f6a3')

print(ord('🚣'))
print(hex(ord('🚣')))

#       0  1  2  3  4          # персональный индекс
#       H  E  L  L  O
#      -5 -4 -3 -2 -1
