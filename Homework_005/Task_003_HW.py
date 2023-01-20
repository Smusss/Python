# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c 5a3b4c -> aaaaabbbcccc
#для проверок 'aaaaabbbccccddddt' '5a3b4c'

def data_compression(data):
    short_data = ''
    count = 1
    for i in range(len(data)-1):
        if data[i] == data[i + 1]:
            if i == len(data) - 2:
                count +=1
                short_data = short_data + str(count) + data[i]
            else: 
                count +=1
        else:
            short_data = short_data + str(count) + data[i]
            count = 1
            if i == len(data) - 2:
                short_data = short_data + str(count) + data[-1]
    return short_data
def data_recovery(data):
    long_data = ''
    for i in range(len(data)):
        if data[i].isdigit():
            long_data = long_data + int(data[i]) * data[i+1]
    return long_data
    
data = '5a3b4c'
print(f'Input data: {data}')
if data[0].isdigit():           # recovery or compression
    long_data = data_recovery(data)
    print(f'Recovered data: {long_data}')
else:
    short_data = data_compression(data)
    print(f'Compressed data: {short_data}')