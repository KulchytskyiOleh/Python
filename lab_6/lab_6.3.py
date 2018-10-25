# Створення прикладних програм на мові Python
# Лабораторна робота №6.3
# Кульчицький Олег, №10

text = input('Введи речення: ')
slovo = text.split()
sn = 0
sr = 0
for s in slovo:
  if s[0] == 'н' or s[0] == 'Н':
    sn  += 1
  if s[-1] == 'р':
    sr += 1
print('sn = {}, sr = {}'.format(sn,sr))
