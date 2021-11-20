n1 = int(input('Введіть число: '))
n2 = 0

while n1 > 0:
    digital =n1 % 10
    print(digital)
    n1 //= 10
    print(n1)
    n2 *= 10
    n2 += digital
print(n2)
