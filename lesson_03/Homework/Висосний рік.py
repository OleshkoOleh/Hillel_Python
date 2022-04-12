# print('Определяем Високосный год')
#
# year = 0
# running = True
#
# while running:
#     guess = int(input('Введи год: '))
#
#     if guess == year / 4:
#         print('Данный год Високосный')
#     elif guess == year / 400:
#         print('Данный год Високосный')
#     else:
#         print('Данный год Невисокосный')
# print(Завершение)

# print('Определяем Високосный год')
#
# year = 2020
#
# if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
#     return True
# else:
#     return False
#
# print('Завершение')

# year = 2020
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     return True
# else:
#     return False

# year = 1700
#
# if year % 400 == 0:
#     print('%d Високосный год' %year)
# elif year % 100 == 0:
#     print('%d Не високосный год' % year)
# elif year % 4 == 0:
#     print ('%d Високосный год' %year)
# else:
#     print ('Не високосный год')

# print('Определение високосного года\n')
#
# year = 1359
#
# if year % 400 == 0:
#     print(year, 'Является високосный год')
# elif year % 100 == 0:
#     print(year, 'Не является високосный год')
# elif year % 4 == 0:
#     print (year, 'Является високосный год')
# else:
#     print (year, 'Является невисокосным годом')
# print('Повторить попытку?')


print('\nОпределение високосного года\n')

year = 1626

if year % 400 == 0:
    print(year, 'год является високосным')
elif year % 100 == 0:
    print(year, 'год является невисокосным')
elif year % 4 == 0:
    print (year, 'год является високосным')
else:
    print (year, 'год является невисокосным')

print('\nВвести другой год?')