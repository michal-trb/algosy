from random import randint
from time import time

def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

length=10000
array=[randint(1,10000) for i in range(length)]
array2 = array.copy()
t0=time()
shellSort(array, len(array))
t1=time()
array2.sort()
t2=time()

if array==array2 :
   print('sortowanie shellSort w czasie', t1-t0)
   print('sortowanie metodą wbudowaną w czasie', t2-t1)
