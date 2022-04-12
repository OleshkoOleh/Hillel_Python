"""
while <condition>:                                          - вычисление условия выражения. Если True - переходим к оператору
    operator 1
    operator 2
    ...
    operator N - любое выражение на True или False
"""

# bool -> True, False
# 0, 0.0, '', "", [], (), {} - False


i = 1
while i <=10:
    print(i, end=' ')
    i += 1
else:
    print('else')

i = 1
while i <=10:
    print(i, end=' ')
    i += 1
    if i ==5:
        break
else:
    print('else')