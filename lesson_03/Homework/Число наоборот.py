print('\nПеревернуть число\n')

num = int(input('Введите целое положительное трехзначное число: '))

print('Результат: ', end=' ')

print(((num % 10) * 100) + (((num // 10) % 10) * 10) + num // 100)

print('Завершение операции')