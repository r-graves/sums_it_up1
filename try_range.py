#import pandas

ls = list(range(0,10))

print(ls)

for i in ls:
    ls[i] = ls[i] + 1

lst = list(range(50,75))

def fun1(lst):
    i = 0
    while i < len(lst):
        lst[i] = lst[i] + 1
        i = i + 1
    return(lst)

print(fun1(lst))


