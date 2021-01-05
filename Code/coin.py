from typing import List

### find min number of coins 

 # 1. slow
def rec(change,coins):
    minCoins = change
    if change in coins:
        return 1
    else:
        for i in [c for c in coins if c <= change]:
            sumCoins = 1 + rec(change-i,coins)
            if sumCoins < minCoins:
                minCoins = sumCoins
    return minCoins

# print(rec(43,[1,2,5,10,25])) 

# 2. more efficient 
def recDC(change:int,coins:List,knownresult:List) -> int:
    '''
    This function aims to find out minimum number of coins 
    '''
    minCoins = change
    if change in coins:
        return 1
    elif knownresult[change] > 0:
        # use knownresult to store values, 
        # if the number of coins have already been calculated
        # the min coins will be stored for further use
        return knownresult[change]
    else:
        for i in [c for c in coins if c <= change]:
            sumCoins = 1 + recDC(change-i,coins,knownresult)
            if sumCoins < minCoins:
                minCoins = sumCoins
                knownresult[change] = minCoins
    return minCoins

# x = 101
# print(recDC(x,[1,5,10,21,25],[0]*(x+1)))




# 3.
def hjcdc(change:int,coins:List,knownresult:List) -> int:
    pass