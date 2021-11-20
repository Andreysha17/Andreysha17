from array import *
myArray = array('i', [-568, -230, 0, -3, -2, 1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10])

min = 0
sum3 = 0
for i in myArray:
    if i % 3 == 0:
        sum3 += i;
for i in myArray:
    if i > min:
        min = i;

print("Мінімальний додатній елемент : ", min)
print("Добуток елементів масиву кратним 3:", sum3)

print("Вивід не нульових елементів : ")
for i in myArray:
    if i != 0:
        print(i)
