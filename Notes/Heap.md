# 9.2 堆 Heap
### 二叉堆
队列有一个重要的变体，叫作优先级队列。和队列一样，优先级队列从头部移除元素，不过元素的逻辑顺序是由优先级决定的。优先级最高的元素在最前，优先级最低的元素在最后。因此，当一个元素入队时，它可能直接被移到优先级队列的头部。就时间复杂度而言，列表的插人操作是 $O(n)$ ，排序操作是$O(nlogn)$ 其实，效率可以更高实现优先级队列的经典方法是使用叫作二叉堆的数据结构。二叉堆的入队操作和出队操作均可达到 $O(logn)$。

二叉堆学起来很有意思，它画出来很像一棵树，但实现时只用一个列表作为内部表示。二叉堆有两个常见的变体：最小堆（最小的元素一直在队首）与最大堆（最大的元素一直在队首） 



### 完全二叉树与堆
#### 结构属性
完全二叉树除了最底层，其他每一层都是满的，在最底层，从左往右填充节点。
完全二叉树可以使用列表来表示，对于列表中处于p位置的节点来说，它的左子节点位于2p，右子节点位于2p+1。
堆的前提是完全二叉树。
#### 堆的有序性：对于堆中任意元素x与其父元素p，x都不大于p
#### 堆操作

- BinaryHeap()新建一个空的二叉堆。初始化
  - 用currentsize记录二叉堆的当前大小
  - 列表Heaplist的第一个元素为0，唯一的目的是可以让后续的方法使用整除法 
- insert(k)往堆中加人一个新元素。
  - percDown(currentsize):  交换根节点与最小子节点
  - minChild(i): 找到最小子节点的index
- findMin()返回最小的元素，元素留在堆中
- delMin()返回最小的元素，并将该元素从堆中移除
  - 把堆顶的元素与最后一个元素交换位置，再把堆的元素借助percDown函数移到正确的位置 
- isEmpty()在堆为空时返回True，否则返回False
- size()返回堆中元素的个数
- buildHeap(list)根据一个列表创建堆。


### 映射抽象数据类型
在实现搜索树之前，我们来复习一下映射抽象数据类型提供的接口。你会发现，这个接口类似于Python字典。

- Map()新建一个空的映射。
- put(key,val)往映射中加入一个新的键一值对。如果键已经存在，就用新值替换旧值。
- get(key)返回key对应的值。如果key不存在，则返回None.
- del 通过del map [key]这样的语句从映射中删除键—值对。
- len()返回映射 存ft键i对的数目。
- in通过key in map这样的语句，在键存在时返回True，否则返回False

Code
```
from typing import List

class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def insert(self,key):
        self.heaplist.append(key)
        self.currentsize = self.currentsize + 1
        self.percUp(self.currentsize)
    
    def percUp(self,i:int):
        while i // 2 > 0 :
            if self.heaplist[i] < self.heaplist[i // 2]:
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i // 2] 
                self.heaplist[i // 2] = temp
            i // 2



    def delMin(self):
        retVal = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.heaplist.pop()
        self.currentsize = self.currentsize - 1
        self.percDown(1)
        return retVal
    def percDown(self,i:int):
        while i * 2 <= self.currentsize:
            mc = self.minChild(i)
            if self.heaplist[mc] < self.heaplist[i]:
                self.heaplist[mc],self.heaplist[i] = self.heaplist[i],self.heaplist[mc]
            i = mc
    def minChild(self,i:int):
        if i * 2 > self.currentsize:
            return self.currentsize
        else:
            if self.heaplist[ i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


    def buildHeap(self,alist:List):
        '''
        Build Heap from unordered list. 
        Time Complexity:O(n)
        '''
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        print(self.heaplist,i)
        while i > 0:
            print(self.heaplist,i)
            self.percDown(i)
            i = i - 1 
        print(self.heaplist,i)
```

