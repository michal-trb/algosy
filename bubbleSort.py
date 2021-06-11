from random import randint
from time import time

def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
  

length=100
array=[randint(1,10000) for i in range(length)]
array2 = array.copy()
t0=time()
bubbleSort(array)
t1=time()
array2.sort()
t2=time()

if array==array2 :
   print('sortowanie bubble sort w czasie', t1-t0)
   print('sortowanie metodą wbudowaną w czasie', t2-t1)
