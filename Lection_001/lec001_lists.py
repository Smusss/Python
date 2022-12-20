numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
    
print(numbers) # [10, 2, 3, 4, 5]


colours = ['red', 'green', 'blue']
print(colours)

for e in colours:
    print(e*2)

colours.append('gray')  #добавить в конец
print(colours == ['red', 'green', 'blue', 'gray'])
colours.remove('red') # delete colours[0]
print(colours)