# range(start, stop, step)
# range(start, stop)            - по умолчанию step =1
# range(stop)                   start = 0,step = 1

# range (1, 10, 2)              - получим 1, 3, 5, 7, 9

# for i in range(1, 25):
#     print(i, end=' ')
# print()

# for i in range(0, 25, 3):
#     print(i, end=' ')
# print()

# for i in range(250, 25, -10):
#     print(i, end=' ')
# print()

# for i in range(25):
#     print(i, end=' ')
# print()

j = 0
for _ in range(10):
    print(j**2, end=' ')
    j += 1
print()