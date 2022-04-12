"""

for <variable> in <iterable 0 obj>:
    operator1
    var1 = variable + 25

for _ in <iterable 0 obj>:
    operator1

"""

for ch in 'Hillel_Python':
    print(ch, end= ' ')
print()

for ch in 'Hillel_Python':
    print(ch, end= ' ')
    if ch == 'h':
        break
print()

for ch in 'Hillel_Python':
    print(ch, end= ' ')
    if ch == 'P':
        continue

for ch in 'Hillel_Python':
    if ch == 'n':
        break
    print(ch, end=' ')
else:
    print('else')
print()

# break
# continue
# else