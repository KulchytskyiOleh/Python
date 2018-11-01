#Описати клас-ітератор, який повертає слова рядка(слова розділяються одним або декількома пропусками) у оберненому порядку слідування

class Reverse:
    def __init__(self, data):
        self._data = data           
        self._index = len(data) 
    def __iter__(self):       
        return self
    def __str__(self):
        return '{}\n'.format(self._data)    
    def __next__(self):       
        if self._index == 0:        
            raise StopIteration    
        self._index = self._index - 1
        return self._data[self._index]
data = Reverse(['Сьогодні','був','','сонячний','','','день','у','','','','нашому','','місті'])
print(data)
for x in data:
    print(x)
