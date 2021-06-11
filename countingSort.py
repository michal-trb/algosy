from random import randint
from time import time

 
def countingSort(A):

    # create counters initialized to zero
    frequencies = [0] * (max(A)+1)

    # count each item
    for value in A:
        frequencies[value] += 1

    # recreate sorted array
    writepos = 0
    for value, count in enumerate(frequencies):
        for i in range(count):
            A[writepos] = value
            writepos += 1

    return A

length=10000
array=[randint(1,10000) for i in range(length)]
array2 = array.copy()
t0=time()
countingSort(array)
t1=time()
array2.sort()
t2=time()

if array==array2 :
   print('sortowanie counting sort w czasie', t1-t0)
   print('sortowanie metodą wbudowaną w czasie', t2-t1)

