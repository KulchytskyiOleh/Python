import random
def f(arg):
    snow = 0; rain = 0
    for day in arg:
        value = arg.get(str(day))
        if value[1] < 0: snow += value[0]
        else: rain += value[0]; 
    return snow, rain
month = {}
for i in range(1,32): month[str(i)] = [random.randint(0,100),random.randint(-40,40)]
res = f(month)
print('{}\nСніг: {}, Дощ: {}'.format(month,res[0],res[1]))
