print('\nМожет ли конь попасть с первой клетки на вторую одним ходом?\n')

coord_x1 = coord_y1 = 0
print('Первая клетка (начало координат) Х=0, Y=0')

coord_x2 = int(input('Вторая клетка. Введите координаты по оси Х: '))
coord_y2 = int(input('Вторая клетка. Введите координаты по оси Y: '))

diff_coord_x = (coord_x1 - coord_x2)
diff_coord_y = (coord_y1 - coord_y2)

if diff_coord_x == 1 and diff_coord_y == 2 or diff_coord_x == 2 and diff_coord_y == 1:
    print('Может')
elif diff_coord_x == -1 and diff_coord_y == -2 or diff_coord_x == -2 and diff_coord_y == -1:
    print ('Может')
else:
    print('Не может')

print('\nЗавершение операции')