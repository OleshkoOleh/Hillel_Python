print('\nОпределение количества новых парт в математических классах\n')

class_room_A = int(input('Введите количество учеников в классе А : '))
class_room_B = int(input('Введите количество учеников в классе В : '))
class_room_C = int(input('Введите количество учеников в классе С : '))

print('Общее количество парт :', end= '' )
print(class_room_A // 2 + class_room_B // 2 + class_room_C // 2 + class_room_A % 2 + class_room_B % 2 + class_room_C % 2)

print('Количество парт в классе А :', end= '' )
print(class_room_A // 2 + class_room_A % 2)

print('Количество парт в классе B :', end= '' )
print(class_room_B // 2 + class_room_B % 2)

print('Количество парт в классе C :', end= '' )
print(class_room_C // 2 + class_room_C % 2)

print('Завершение вычисления')


