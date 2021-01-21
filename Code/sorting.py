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
                

def selectionSort(alist):
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



def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue


def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startposition in range(sublistCount):
            gapInsertionSort(alist,startposition,sublistCount)
        print("After increments of size ", sublistCount, " The list is ",alist)
        sublistCount = sublistCount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start + gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue



def mergeSort(alist):
    pass

def heapSort(alist):
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