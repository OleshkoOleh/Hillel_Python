# for i in range(0, 50, 5):
#     print(i)
# else:
#     print('No data')

# while True:
#     s = input('Type something: ')
#     if s == ('Выход'):
#         break
#     print('Длина строки:', len(s))
# print('Game over?')

while True:
    s = input('Введите что - нибудь: ')
    if s == 'выход':
        break
    if s == 'Выход':
        break
    if len(s) < 5:
        print('Слишком малое значение')
        continue
    print('Введенная строка нужной длины')