from typing import List


'''
def numCoin(money,coinList):
    numofCoin = []
    while money > 0:
        for coin in coinList:
            if money >= coin and money % coin == 0:
                numofCoin.append(money % coin)
        a = max(coinList)
        if money > a:
            numCoin(money-a,coinList)
        else:
            coinList = coinList[:-1]
        return max(numCoin)

money = 63
coinList = [1,5,10,21,25]
print(numCoin(money,coinList))
'''



def recMC(coinList:List,change:int,knowResult) -> int:
    '''
    This function will return the least number of coins used to give the change.
    '''
    minCoins = change
    if change in coinList:
        knowResult[change] = 1
        return 1
    elif knowResult[change] > 0 :
        return knowResult[change]
    else:
        for i in [c for c in coinList if c <= change]:
            numCoins = 1 + recMC(coinList,change-i,knowResult)
        if numCoins < minCoins:
            minCoins = numCoins
            knowResult[change] = minCoins
    return minCoins

coinList = [1,5,10,21,25]
change = 63
knowResult = 64 * [0]
print(recMC(coinList,change,knowResult))