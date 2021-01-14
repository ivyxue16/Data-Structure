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
print(sequentialSearch(testlist,42))
# print(sequentialSearch(testlist,18))

