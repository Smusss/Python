#def sum(x,y):
    #return x + y

sum = lambda x, y: x + y # то же самое что в 1 - 2 стр

def mylt(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    return op(a,b)
calc(mylt, 4, 5)

calc(lambda x, y: x + y, 4, 5) # то же самое что в 12 стр


list1 = []
for i in range(1,21):
    if (i % 2 ==0):
        list1.append(i)
print(list1)

list1 = [i for i in range(1, 21) if i % 2 == 0]
print(list1)
list1 = [(i, i) for i in range(1, 21) if i % 2 == 0] # список кортежей
print(list1)

def f(x):
    return x**3

list1 = [(i,f(i)) for i in range (1, 21) if i % 2 == 0] #список кортежей 
print(list1)

# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38 Получить:[(2, 4), (8, 64), (38, 1444)]

f = open ('ID.txt','r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e,e**2))
print(out)




def select (f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split(' ')
res = select(int,data)
res= where(lambda x: not x % 2, res)
res = select(lambda x: (x, x **2), res)
print (res)




li = [x for x in range(1,20)]
li = list(map(lambda x: x + 10, li))
print (li)

data = list(map(int, input().split()))
print(data)

data = '1 2 3 5 8 15 23 38'.split(' ')
res = map(int,data)
res= where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x **2), res))
print (res)

data = '1 2 3 5 8 15 23 38'.split(' ')
res = map(int,data)
res= list(filter(lambda x: not x % 2, res))
res = list(map(lambda x: (x, x **2), res))
print (res)

users = ['us1', 'us2', 'us3']
ids = [1, 2, 3,]
data = list(zip(users, ids))
print (data)

data = list(enumerate(users))
print(data)