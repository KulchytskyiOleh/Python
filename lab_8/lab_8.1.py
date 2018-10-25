def hanoi(n, d_1, d_2, d_3) :
  if (n == 0) : return
  hanoi(n-1,d_1,d_3,d_2)
  print('Диск',n,'переміщений з', d_1, 'на' ,d_2)
  hanoi(n-1,d_3,d_2,d_1)
n = int(input('Введіть N = '))
hanoi(n,1,2,3)
print('Кількість переміщень при N =', n, ' -- ',2**n-1)
