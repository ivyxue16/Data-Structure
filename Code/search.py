from typing import List

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

# print(sequentialSearch(testlist,42))
# print(sequentialSearch(testlist,18))

