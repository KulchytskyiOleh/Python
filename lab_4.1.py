# Створення прикладних програм на мові Python
# Лабораторна робота №4
# Кульчицький Олег, №10
print ('Створення прикладних програм на мові Python, Лабораторна #4.1')
print ('Кульчицький Олег, №10')
eps = 10E-4
n = 1
a = 1 / 3
suma = a
while a > eps:
	n +=  1 
	c = 1
	z = 1
	for x in range(1, n+1):
		c *= x
		z *= 3 * x**x
	a = c / z
	suma += a
print('При n = {}, a[n] = {} < {} ,і сума всіх елементів буде рівна s = {}'.format(n,a,eps,suma))