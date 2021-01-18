from typing import List

def bubbleSort(alist:List):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]: 
                # temp = alist[i+1]
                # alist[i+1] = alist[i]
                # alist[i] = temp
                alist[i],alist[i+1] = alist[i+1],alist[i]   # Python supports direct change
                

alist = [54,26,93,17,31,44,55,20]
bubbleSort(alist)
# print(alist)

def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue

alist = [54,26,93,17,31,44,55,20]
insertionSort(alist)
print(alist)