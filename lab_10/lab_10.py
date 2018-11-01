class Region:
  def __init__(self, name, area, peoples, *city):
    self.name = name
    self.area = area
    self.peoples = peoples
    self.city = city
  def hust(self):
    ro = self.peoples/self.area
    return ro 
  def inSearch(self,name):
    if name == self.name:
      print('Площа:',self.area)
      print('Населення:',self.peoples)
      print('Густота населення:',self.peoples/self.area)
      print('Міста:',end=' ')
      for x in self.city:
        print(x,end=', ')
    elif name in self.city:
      print(self.name)
    else:
      print('Nema!')
def sort(*sp):
  a = []
  for x in sp:
    a.append(x)
  l = len(a)
  for i in range(l):
    for j in range(i,l):
      if a[i][1] < a[j][1]:
        a[i],a[j] = a[j],a[i]
  for i in range(l):
    print(a[i])
 
i_f = Region('Івано-Франківська',13928, 1382658, 'Болехів','Калуш','Долина','Бурштин','Івано-Франківськ')
lviv = Region('Львівська',21833,2529608,'Стрий','Червоноград','Самбір','Дрогобич','Борислав')
tern = Region('Тернопільська',13823,1059200,'Бережани','Тернопіль','Чортків','Кременець')
dnipro = Region('Дніпропетровська',31914,3230400,'Дніпро','Нікополь','Марганець')
kyiv = Region('Київська',28131,1734500,'Київ','Бориспіль','Вишгород','Бровари')
vol = Region('Волинська',20143,1041000,'Ковель','Луцьк','Нововолинськ')
regions = []
spisok = []
regions.append(i_f)
regions.append(lviv)
regions.append(tern)
regions.append(dnipro)
regions.append(kyiv)
regions.append(vol)

name = input('Введіть назву: ')

for x in regions:
  spisok.append([x.name, x.hust()])
  if (name in x.name) or (name in x.city):
    x.inSearch(name)

flag = input('\nВідсортувати області за густотою населення? (y/n): ')
if (flag == 'y'):
  sort(*spisok)
else:
  pass
