from random import randint
from time import time

def combblb(A):
    global licz; licz=0
    grab = len(A)
    guard = True
    while guard or grab>1:
        grab = grab*10//13
        if grab<1 : grab =1
        guard = False
        for i in range(len(A)-grab):
            if A[i] > A[i + grab]:
                A[i], A[i + grab] = A[i + grab], A[i]
                licz +=1; guard = True

    return A

length=10000
array=[randint(1,10000) for i in range(length)]
array2 = array.copy()
t0=time()
combblb(array)
t1=time()
array2.sort()
t2=time()

if array==array2 :
   print('sortowanie comb sort w czasie', t1-t0)
   print('sortowanie metodą wbudowaną w czasie', t2-t1)

