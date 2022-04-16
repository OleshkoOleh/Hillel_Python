# # +, *, / -  оператор
#
# # A, B - операнд
#
# # A+B=C - выражение
#
# s1 = 'Hello'
# s2 = 'World!'
#
# s3 = s1 + ' ' + s2
# print(s3)
# print(s3*8)
# print(165/8)
# print(165//165)




# print ('all')
#
# n = int(input('Введите число: ' ))
# m = 0
# while n>0:
#     m=m*10 + n%10
#     n = n // 10
# print (m)
# print('END')



num = int(input('Start: '))
b = 0

b = num % 10;
num = num // 10;
b = num + (b * 100);

b = num % 10;
num = num // 10;
b = num + (b * 100);



print(b)
print('End')