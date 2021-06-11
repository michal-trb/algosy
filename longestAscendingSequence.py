from random import randint


def findSequence(array):
    currentIndex = 1
    currentSequence = [array[0]]
    sequences = []

    while currentIndex < len(array):
        if array[currentIndex - 1] < array[currentIndex]:
            currentSequence.append(array[currentIndex])
        else:
            if len(currentSequence) > 0:
                sequences.append(currentSequence)
            currentSequence = [array[currentIndex]]

        currentIndex += 1

    sequences.append(currentSequence)
    return sequences


length = 10000
array = [randint(1, 10000) for i in range(length)]
sequences = findSequence(array)

print('Ciąg: ', array)
print('Ciągi rosnące: ', sequences)
print('Najdłuższy ciąg (lub pierwszy najdłuższy w przypadku kilku o tej samej długości):', max(sequences, key=len))
print('Ciąg z najwyższą sumą liczb:', max(sequences, key=sum))
