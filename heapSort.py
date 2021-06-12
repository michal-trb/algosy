from random import randint
from time import time


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


length = 10000
array = [randint(1, 10000) for i in range(length)]
array2 = array.copy()

t0 = time()
heapSort(array)
t1 = time()
array2.sort()
t2 = time()

if array == array2:
    print('sortowanie kubełkowe w czasie', t1 - t0)
    print('sortowanie metodą wbudowaną w czasie', t2 - t1)
