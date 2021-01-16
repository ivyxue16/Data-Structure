from typing import List
import numpy as np


def sequentialSearch(searchList:List, item):
    pos = 0
    found = False

    while pos < len(searchList) and not found:
        if searchList[pos] == item:
            return True
        else:
            pos += 1
    return found


testlist = [1,2,32,8,17,19,42,13,0]
# testlist = np.random.randint(0,100,10)
# print(testlist)
# print(sequentialSearch(testlist,42))
# print(sequentialSearch(testlist,18))



def binarySearch(alist:List,item:int) -> bool:
    '''
    Input parameters:
    alist: search list, in ascending order
    item: the target
    '''

    first = 0
    last = len(alist) - 1

    found = False

    while first <= last and not found: # not found must be included
        mid = (first + last) // 2 
        print(mid,first,last)
        if alist[mid] == item:
            return True
        else:
            if alist[mid] < item:  
                first = mid + 1 
            else: 
                last = mid  - 1
    return found


testlist = [1,2,32,8,17,19,42,13,0]
# print(binarySearch(testlist,41))