# коммент
value = None
a = 123
b = 5.56
print (type(a))
print (type(b))
value = "'oppa'"
b = '12nmb34'
print (type(value))
print (value)
print (a, ' + ', b, ' = ')
print (a, b, value)
print (a, '-', b,'-', value)
print ('{} - {} - {}'.format(a, b, value))
print (f'{a} - {b} - {value}')
print ('{2} - {0} - {1}'.format(a, b, value))
f = True
print (f)
list = [1, 2, 'wow']
print (list)

print ('Input c:')
c = int(input())
print ('it is c: ', c)
d = 'aaa'
e = 'aaa'
print (d == e)
f = [1,2, 3, 4]
print (2 in f)
is_odd = f[0] % 2 == 0
print(is_odd)

is_odd = not f[0] % 2
print(is_odd)


g = int(input('g = '))
h = int(input('h = '))
if g > h:
    print(g)
else:
    print(h)

original = 23
inverted = 0
print (original)
while original !=0:
    inverted = inverted * 10 +(original % 10)
    original //=10
else:
    print ('Enough!')
print (inverted)

for i in 1, 2, 3, 4, 5:
    print(i**2)
list_2 = [10, 9, 8]
for i in list_2:
    print(i)

r = range(10)
for i in r:
    print(i)

for i in range(5):
    print(i)

for i in range(1, 10 , 2):
    print(i)
for i in 'qwertyu':
    print(i)