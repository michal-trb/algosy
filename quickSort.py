from random import randint
from time import time


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


length = 10000
firstArray = [randint(1, 10000) for i in range(length)]
secondArray = firstArray.copy()
t0 = time()
quicksort(firstArray)
t1 = time()
secondArray.sort()
t2 = time()

print(firstArray)
print(secondArray)

if firstArray == secondArray:
    print('sortowanie quicksort w czasie', t1 - t0)
    print('sortowanie metodą wbudowaną w czasie', t2 - t1)
