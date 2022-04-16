# """
# while <condition>:                                  - вычисление условия выражения. Если True - переходим к оператору
#     operator 1
#     operator 2
#     ...
#     operator N - любое выражение на True или False
# operatorM
# """

# В операторе While можно применять формулы

# bool -> True, False
# 0, 0.0, '', "", [], (), {} - False

# -------------------------------------------------------------
# Пример - 1

# i = 1
# print(i**2)
# i += 1
# print(i**2)
# i += 1
# print(i**2)
# i += 1
# print(i**2)
# i += 1
# print(i**2)

# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1

# -------------------------------------------------------------
# Пример - 2
# Счетчик подсчета количества символов

# num = int(input('Введите целое число: '))
# cnt = 0
# while num != 0:
#     cnt += 1
#     num //= 10
#
# print(cnt)

# -------------------------------------------------------------
# Пример - 3 - Бесконечный цикл. Прерывание цикла
# Счетчик подсчета количества символов

# num = int(input('Введите целое число: '))
# cnt = 0
# while True:
#     cnt += 1
#     num //= 10
#     if num == 0:
#         break
# print(cnt)

# -------------------------------------------------------------
# Пример - 4.1 - Прерывание цикла.
# Счетчик подсчета количества символов

# num = int(input('Введите целое число: '))
# while num != 0:
#     x = num % 10
#     num //= 10
#     if x % 2 == 0:
# print(x)


# Пример - 4.2 - Прерывание цикла.
# Нечетные числа

# num = int(input('Введите целое число: '))
# while num != 0:
#     x = num % 10
#     num //= 10
#     if x % 2 != 0:     # Условие проверяет цифру на нечетность
#         continue
#     print(x)

# ------------------------------------------------------------
# Пример - 5.1 - Прерывание цикла.
#
# i = 1
# while i < 10:
#     print(i, end=' ')
#     i += 1
# else:
#     print('else')

# Пример - 5.2 - Прерывание цикла. Если вышли через break операция else не выполняется
#
# i = 2
# while i < 10:
#     print(i, end=' ')
#     i += 1
#     if i == 5:
#         break
# else:
#     print('else')