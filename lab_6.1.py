# Створення прикладних програм на мові Python
# Лабораторна робота №6.1
# Кульчицький Олег, №10

arr = []
n = int(input('Кількість чисел: '))
for i in range(n):
	print(i+1,') ',end =' ')
	arr.append(input())
k = len (arr)
pary = []
count = 0
for i in range(k-1):
	for j in range(i+1,k):
		if i in pary or j in pary:
			continue
		else:
			if arr[i] == arr[j]:
				pary.append(i)
				pary.append(j)
				count += 1
print(count,'пар')
