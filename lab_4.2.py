# Створення прикладних програм на мові Python
# Лабораторна робота №4
# Кульчицький Олег, №10
print ('Створення прикладних програм на мові Python, Лабораторна #4.2')
print ('Кульчицький Олег, №10')
number = int(input ('Введіть число: '))
t = 1
k = 0
while  True:
	if number / t < 1:
		break
	else:
		t *= 10
		k += 1
print('Кільскість цифр - ', k)