# number = 23
# running = True
#
# while running:
#     guess = int(input('Введите целое число: '))
#
#     if guess == number:
#         print('Поздравляю, вы угадали.')
#         running = False
#     elif guess < number:
#         print('Нет! Загаданное число немного больше этого.')
#     else:
#         print('Нет! Загаданное число немного меньше этого.')
#
# print('Завершение')


number = 4
running = True

while running:
    guess = int(input('Введи число: '))

    if guess == number:
        print('Fuck yes!')
        running = False
    elif guess < number:
        print('Fuck low!')
    else:
        print('Fuck high!')
else:
    print('Done. Try again!')
print('Game over?')