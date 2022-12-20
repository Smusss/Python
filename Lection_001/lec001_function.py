def f(x):
    return x**2

def f(x):               #print(f(1)) # Целое
    if x == 1:          #print(f(2.3)) # 23
        return 'Целое'  #print(f(28)) # None
    elif x == 2.3:      #print(type(f(1))) # str
        return 23       #print(type(f(2.3))) # int
    else:               #print(type(f(28))) # NoneTyp
        return

arg = 1
print(f(arg))
print(type(f(arg)))
