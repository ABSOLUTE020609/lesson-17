import random
import hashlib
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 100]
result = []
for number in numbers:
    if number > 5 and number < 50:
        result.append(number)
print(result)

a = []
for i in range(1, 15):
    a.append(i)
print(a)
result = filter(lambda number:number > 5 and number < 50, numbers)
print(list(result))

result1 = [number for number in numbers if number > 5 and number <50]
print(result1)

b = [2009, 2010, 2011, 2012,2013,2014,2015]
c = []
for number in b:
    if number < 2012 and number > 2009:
        c.append(number)
print(c)

names = ['leo', 'max']
names_upper = [name.upper() for name in names]
print(names_upper)
names_m = [name for name in names if name[0]=='m']
print(names_m)

result01 = [1 if number > 5 else 0 for number in numbers]
print(result01)

result011 = {random.randint(a = 1,b = 100) for i in range(10)}
print(result011)

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())
