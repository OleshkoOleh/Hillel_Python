# """
# 1
# for <variable> in <iterable 0 obj>:   # Итерабельный объект можно перебрать по элементам, посимвольно. Например "строку". В том числе генераторы
#     operator1
#     var1 = variable + 25
# 2
# for _ in <iterable 0 obj>:           # Итерабельный объект без переменной можно перебрать по элементам, посимвольно. Например "строку". В том числе генераторы
#     operator1
#
# """


# ----------------------------------------------------------
# Пример - 1


for ch in 'Hillel_Python':
    print(ch, end= ' ')
print()

# ----------------------------------------------------------
# Пример - 2

for ch in 'Hillel_Python':
    print(ch, end= ' ')
    if ch == 'h':
        break
print()

# ----------------------------------------------------------
# Пример - 3

for ch in 'Hillel_Python':
    if ch == 'P':
        continue
    print(ch, end = ' ')

# Пример - 3.1

for ch in 'Hillel_Python':
    if ch == 'l':
        break
    print(ch, end = ' ')
else:
    print('else')
print()
