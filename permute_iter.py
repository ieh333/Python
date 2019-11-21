from time import *
from itertools import permutations
str=input("Vavedete niz ot chisla:\n")
lst=list(str)
t1=time()
perm=permutations(lst)
t2=time()
t=t2-t1
for i in perm:
    print(i)
print(t)
