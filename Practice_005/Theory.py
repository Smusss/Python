from random import randint as RI  
my_list = [RI(0,10) for _ in range(10)]
print(my_list)

orig_text = 'Питон наабвверное самый лучший их хуабвдших языков'
orig_list = []
for i in orig_text.split():
    if not 'абв' in i:
        orig_list.append(i)
    else:
        orig_list.append('***')
print(' '.join(orig_list))

print(' '. join(list(filter(lambda x: not 'абв' in x, orig_text.split()))))
