# 6.2  贪心算法Greedy algorithm 和动态规划 Dynamic Programming

### 硬币找零问题
找零时使用最少的硬币
input: 找零金额，可以使用的硬币面值
output: 最少的硬币个数

### 贪心算法
试图最大程度地解决问题。在找零时使用最少的硬币，使用贪心算法，该先使用面值最大的硬币，使用尽可能多的该硬币，然后再尽可能多的使用面值第二大的硬币。

对于美国的硬币来说，贪心算法总能找到最优解，但是除了常见的1,5,10,25外还有21分的硬币，如果找零金额为63分，那么贪心算法则无法得到最优解。


### 递归
使用递归算法：
- 基本情况：如果要找的零钱金额与硬币面值相同，则只需要1枚硬币
- 如果要找的零钱金额与硬币面值不相同，则有多种选择：
  - 1枚1分的硬币加上找零金额减去1分之后所需要的硬币
  - 1枚5分的硬币加上找零金额减去5分之后所需要的硬币
  - 1枚10分的硬币加上找零金额减去10分之后所需要的硬币
  - 1枚25分的硬币加上找零金额减去25分之后所需要的硬币

如下所示：  
```
numCoins = min(1+numCoins(originalamount-1),
               1+numCoins(originalamount-5),
               1+numCoins(originalamount-10),
               1+numCoins(originalamount-25))
```


### 递归代码
```
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
```
![IMAGE](quiver-image-url/4FD9A556506ECD252A45A0F406B2494D.jpg =1017x391)

使用递归算法效率非常低，针对找零金额为63分需要进行67 716 925次调用才能找到最优解。主要的问题是重复计算量太大，这个算法将大量的时间和资源浪费在重复计算已有的结果上。

减少计算量的关键是记住已经计算过的结果，可以将已经计算过的最少硬币数储存在列表中，在计算最小硬币数之前检查是否在表中已经出现了这个结果，如果是，就直接调用。

### 改进代码
使用了一个list存储已经计算过的所需零钱所需个数
```
def recDC(change:int,coins:List,knownresult:List) -> int:
    minCoins = change
    if change in coins:
        return 1
    elif knownresult[change] > 0:
        return knownresult[change]
    else:
        for i in [c for c in coins if c <= change]:
            sumCoins = 1 + rec(change-i,coins)
            if sumCoins < minCoins:
                minCoins = sumCoins
                knownresult[change] = minCoins
    return minCoins

print(recDC(63,[1,5,10,21,25],[0]*64))
```

knownresult中含有一些空白的部分，在改进代码中使用了记忆化(缓存)的方法来优化程序的性能，而不是使用了动态规划。

### 动态规划
动态规划从1分找零开始，系统地一直计算到所需的找零金额，这样可以保证在每一步都已经知道任何小于当前值的找零金额所需要的硬币数。

从1分开始，只需要1枚硬币
2分只需要2枚硬币
找零为5分时，有两个可选方案：要么找5枚1分硬币，要么找1枚5分硬币，通过查表，4分所需要的最少硬币数为4枚，加上1枚1分的硬币，总共5枚，如果直接使用5分的硬币，则最少硬币数为1枚。


![IMAGE](quiver-image-url/9842A761386A37DCBE33B8E034B40FBF.jpg =679x507)

![IMAGE](quiver-image-url/FA911C9A1115EC95DA2551F92ABDB131.jpg =793x258)

找零11分时的三个备选方案：
- 1枚1分硬币加上10分零钱(11-1)最少需要的硬币个数(1个)
- 1枚5分硬币加上6分零钱(11-5)最少需要的硬币个数(2个）
- 1枚10分硬币加上1分零钱(11-1)最少需要的硬币个数(1个)

### 动态规划Code
```
def dpCoins(change:int, coins:List,minCoins:List) -> int:
    for cent in range(1,change+1):
        coinCount = cent
        for i in [c for c in coins if c <= cent]:
            if minCoins[cent-i] + 1 <= coinCount:
                coinCount = minCoins[cent-i] + 1
        minCoins[cent] = coinCount
    return minCoins[change]
```

实际工作中需要记录最少找零具体使用哪个硬币，可以打印出具体使用的硬币面值
### 动态规划修改后的Code
```
def dpCoins3(change:int, coins:List,minCoins:List,coinUsed) -> int:
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

def printCoin(coinUsed:List,change:int):
    '''
    Print which coin is used when calculating minimum number of coins
    '''
    coin = change
    while coin > 0:
        thiscoin =  coinUsed[coin]
        print(thiscoin)
        coin = coin - thiscoin

c1 = [1,5,10,25,21]
coinUsed = [0]*64
coinCount = [0]*64
dpCoins3(63, c1,coinCount,coinUsed)

# coinUsed is updated after calling function 'dpCoins3' 
printCoin(coinUsed,63) 

```