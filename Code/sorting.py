from typing import List

def bubbleSort(alist:List):
    '''
    Time Complexity: O(n^2)
    '''
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]: 
                # temp = alist[i+1]
                # alist[i+1] = alist[i]
                # alist[i] = temp
                alist[i],alist[i+1] = alist[i+1],alist[i]   # Python supports direct change
                

def selectionSort(alist:List):
    '''
    Time Complexity: O(n^2)
    '''
    for i in range(len(alist)-1,0,-1):
        posMax = 0
        for loc in range(1,i+1):
            if alist[loc] > alist[posMax]:
                posMax = loc
        temp = alist[i]
        alist[i] = alist[posMax]
        alist[posMax] = temp



def insertionSort(alist:List):
    for i in range(1,len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue


def shellSort(alist:List):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startposition in range(sublistCount):
            gapInsertionSort(alist,startposition,sublistCount)
        print("After increments of size ", sublistCount, " The list is ",alist)
        sublistCount = sublistCount // 2

def gapInsertionSort(alist:List,start:int,gap:int):
    for i in range(start + gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue




def mergeSort(alist:List):
    print('Splitting ',alist)
    if len(alist) > 1:
        mid = len(alist) // 2 
        leftlist = alist[:mid]
        rightlist = alist[mid:]

        mergeSort(leftlist)
        mergeSort(rightlist)

        i = 0
        j = 0
        k = 0
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k] = leftlist[i]
                i = i + 1
            else:
                alist[k] = rightlist[j]
                j = j + 1
            k = k + 1
        
        while i < len(leftlist):
            alist[k] = leftlist[i]
            i = i + 1
            k = k + 1
        
        while j < len(rightlist):
            alist[k] = rightlist[j]
            j = j + 1
            k = k + 1
        
        print('Merging ', alist)


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    '''
    Use recursion to sort list with smaller size
    '''
    if first < last:
        splitPoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitPoint-1)
        quickSortHelper(alist,splitPoint+1,last)

def partition(alist,first,last):
    pivotValue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while alist[leftmark] <= pivotValue and leftmark <= rightmark:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotValue and leftmark <= rightmark:
            rightmark = rightmark - 1
        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
        
    alist[first], alist[rightmark] = alist[rightmark],alist[first]

    return rightmark





def heapSort(alist:List):
    pass





if __name__ == "__main__":
    alist = [54,26,93,17,31,44,55,20]
    # bubbleSort(alist)
    # print(alist)

    # selectionSort(alist)
    # print(alist)

    # insertionSort(alist)
    # print(alist)

    # shellSort(alist)
    # print(alist)

    # mergeSort(alist)
    # print(alist)

    quickSort(alist)
    print(alist)