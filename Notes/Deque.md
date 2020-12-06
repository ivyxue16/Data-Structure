# 4.5 双端队列 Deque
### 双端队列的定义
双端队列是一种有序的数据结构，与队列类似，其两端可以称作首端和尾端，但deque中数据可以从两端加入，也可以从两端移除，双端队列集成了队列和栈的能力。

### deque定义的操作：
**Deque()**: 创建一个空双端队列
**addFront**: 将item加入队首
**addRear(item)**:将item加入队尾
**removeFront()**:从队首移除数据项，返回值为移除的数据项
**removeRear()**:从队尾移除数据项，返回值为移除的数据项
**isEmpty()**:返回deque是否为空
**size()**:返回deque中包含数据项的个数

**Deque操作例子**
|Deque Operation|Deque Contents|Return Value|
|:-----|:-----|:-----|
|s = Deque()|[]|Deque Object|
|s.isEmpty()|[]|True|
|s.addRear(4)|[4]||
|s.addRear('dog')|['dog',4]||
|s.addFront('cat')|['dog',4,'cat']||
|s.addFront(True)|['dog',4,'cat',True]||
|s.size()|['dog',4,'cat',True]|4|
|s.isEmpty()|['dog',4,'cat',True]|False|
|s.addRear(8.4)|[8.4,'dog',4,'cat',True]||
|s.removeRear()|['dog',4,'cat',True]|8.4|
|s.removeRear()|['dog',4,'cat']|True|

### Python实现Deque
采用List实现，List下标0作为deque的尾端，List下标-1作为deque的首端
操作复杂度：
addFront/removeFront O(1)
addRear/removeRear O(n)

```
class Deque():
    def __init__(self):
        self.items = []
    def addFront(self,item):
        return self.items.append(item)
    def addRear(self,item):
        return self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
```

### 双端队列应用
回文词： radar、madam、toot
中文：上海自来水来自海上、山东落花生花落东山

用双端队列解决回文词问题：
- 先将需要判定的词从队尾加入deque
- 再从两端同时移除字符判定是否相同，直到deque中剩下0个或1个字符

Code:
```
from ADT_Deque import Deque
def palChecker(aString:str) -> bool:
    d = Deque()
    # generate a new deque to store the string
    for ch in aString:
        d.addRear(ch)
    
    stillEqual = True

    while d.size() > 1 and stillEqual:
        """
        when there are more than 1 character in string, loop 
        """
        # the first character and the last character of palindromic are the same
        front = d.removeFront()
        last = d.removeRear()
        if front != last:  
            stillEqual =  False 
            break
    return stillEqual

print(palChecker("lsdhf"))
print(palChecker('radar'))
print(palChecker('toot'))
```





