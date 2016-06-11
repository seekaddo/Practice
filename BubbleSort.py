"""
trying to implement the bubblesort arrays in python
the Pseudo-code from Wikipedia
func bubblesort( var a as array )
    for i from 1 to N
        for j from 0 to N - 1
           if a[j] > a[j + 1]
              swap( a[j], a[j + 1] )
end func

"""

array = [3, 9, 2, 6, 1, 5, 34, 3, 2, 2, 3, 4, 23, 342, 3, 4, 23, 323, 43, 32, 33]
listOne = [3, 9, 2, 6, 1]
listTwo = [4, 8, 5, 7, 0]


def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                swap = array[j]
                array[j] = array[j + 1]
                array[j + 1] = swap
    print(array)


bubblesort(listOne)
bubblesort(listTwo)
