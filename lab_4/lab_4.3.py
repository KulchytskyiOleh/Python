# Створення прикладних програм на мові Python
# Лабораторна робота №4
# Кульчицький Олег, №10
print ('Створення прикладних програм на мові Python, Лабораторна #4.3')
print ('Кульчицький Олег, №10')
a = int(input ('Введіть: a = '))
x1 = 2
eps = 10E-4
if a < 0:
	print('Число повинне бути додатнім!')
else:
	while  True:
		x2 = (x1 + a / x1) / 2
		if abs(x2 - x1) < eps:
			break
		else:
			x1 = x2
print("Корінь від 'a' за ітараційною формулою Герона: а = ", x2)
