# Створення прикладних програм на мові Python
# Лабораторна робота №3
# Кульчицький Олег, №9
from math import *
print ("Створення прикладних програм на мові Python, Лабораторна №3")
print ("Кульчицький Олег, №9")
print ("Введіть змінні:")
x = float(input("x = "))
b = float(input("b = "))
c = float(input("c = "))

if not (sqrt(x-b)) or not abs(x-c):
	print("Значення змінних виходять за область визначення функції!")
else:
	res = (2*x - c) / (sqrt(x-b)) + (abs(x-c))
	print("Результат обчислення = ", res)
