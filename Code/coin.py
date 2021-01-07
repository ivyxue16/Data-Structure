from typing import List

### Find min number of coins 

 # 1. recursion --  very slow 
 # Redundant computations
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

# 2. recursion -- more efficient 
# keep record of calculated number of coins
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

# change = 101
# print(recDC(x,[1,5,10,21,25],[0]*(change+1)))




# 3. Dynamic Programming -- fast
# not recursion
def dpCoins(change:int, coins:list,minCoins:list) -> int:
    for cent in range(1,change+1):
        coinCount = cent
        for i in [c for c in coins if c <= cent]:
            if minCoins[cent-i] + 1 <= coinCount:
                coinCount = minCoins[cent-i] + 1
        minCoins[cent] = coinCount
    return minCoins[change]


# print(dpCoins(63,[1,5,10,21,25],[0] * 64))

## Dynamic programming
def dpCoins2(change:int, coins:list) ->int:
    minCoins = [float('inf')] * (change + 1)
    minCoins[0] = 0
    for cent in range(1,change+1):
        for i in [c for c in coins if c <= change]:
            minCoins[cent] = min(minCoins[cent], minCoins[cent-i] + 1)
    if minCoins[change] != float('inf'):
        return minCoins[change]
    else:
        return -1

# print(dpCoins2(5,[2])) 
# print(dpCoins2(63,[1,5,10,21,25]))

### Print coin used
def dpCoins3(change:int, coins:list,minCoins:list,coinUsed) -> int:
    '''
    Use dynamic programming to calculate the minimum number of coins and which coins are used
    '''
    for cent in range(1,change+1):
        coinCount = cent
        newcoin = 1
        for i in [c for c in coins if c <= cent]:
            if minCoins[cent-i] + 1 <= coinCount:
                coinCount = minCoins[cent-i] + 1
                newcoin = i
        minCoins[cent] = coinCount
        coinUsed[cent] = newcoin
    return minCoins[change]


def printCoin(coinUsed:list,change:int):
    '''
    Print which coin is used when calculating minimum number of coins
    '''
    coin = change
    while coin > 0:
        thiscoin =  coinUsed[coin]
        print(thiscoin)
        coin = coin - thiscoin

# c1 = [1,5,10,25,21]
# coinUsed = [0]*64
# coinCount = [0]*64
# dpCoins3(63, c1,coinCount,coinUsed)

# printCoin(coinUsed,63) # coinUsed is updated after calling function 'dpCoins3' 
