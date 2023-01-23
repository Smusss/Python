path = r'Practice_006\text.txt'

file = open(path,'r', encoding ='UTF-8')
file = file.read()
print(file)

file = open(path,'r', encoding ='UTF-8')
file = file.readline()
print(file)

file = open(path,'r', encoding ='UTF-8')
file = file.readlines()
print(file)

data = 'new text in this file'
file = open(path,'w', encoding ='UTF-8')
new_file = file.write(data)
file.close()

data = 'new text\n in this file'
with open(path,'w', encoding ='UTF-8') as file:
    new_file = file.write(data) 