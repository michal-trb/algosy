from random import uniform
from time import time

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


length=10000
array=[uniform(0,1) for i in range(length)]
array2 = array.copy()
t0=time()
bucketSort(array)
t1=time()
array2.sort()
t2=time()

if array==array2 :
   print('sortowanie bucket sort w czasie', t1-t0)
   print('sortowanie metodą wbudowaną w czasie', t2-t1)

