from time import *
from permute import *
str=input("Vavedete niz ot chisla:\n")
lst=list(str)
t1=time()
l=permute(lst)
t2=time()
t=t2-t1
print(l)
print(t)
