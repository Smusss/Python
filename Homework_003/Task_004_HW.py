# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101   3 -> 11   2 -> 10
def input_number():
    while True:
        try:
            N = int(input("Input number: "))
            return N
        except:
            print("Uncorrect input. Try again")
decimal_N = input_number()
print(bin(decimal_N))
print(decimal_N, end=' ')
binar_N = ''
while decimal_N != 0:
    binar_N = str(decimal_N % 2) + binar_N
    decimal_N = int(decimal_N / 2)
print(f'-> {binar_N}')