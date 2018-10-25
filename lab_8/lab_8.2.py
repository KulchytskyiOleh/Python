def show_x(*x):
  print('x = ',end='')
  for a in x:
    print(a,end=' ')
  print()

def show_y(**y):
  print('y = ',end='')
  for b in y:
    print(y[b],end=' ')
  print()

def f_sum(*x,**y):
  a = []
  b = []
  suma = 0
  for n in x:
    a.append(n)
  for m in y:
    b.append(y[m])
  x0 = a.pop(0)
  for i in range(len(a)):
    dob_y = 1
    for j in range(i+1):
      dob_y *= b[j]
    suma += a[i] + dob_y
  suma += x0
  return suma

tuple = (1,2,3,4,5)
dict = {'one':3,'two':4,'three':5,'four':6}
show_x(*tuple)
show_y(**dict)
print('f =',f_sum(*tuple,**dict))
