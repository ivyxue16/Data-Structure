# 7.3 冒泡排序和选择排序

### 冒泡排序
每次循环中比较相邻的元素，将不合顺序的交换，把最大值放在列表的最后。如果列表中有n个元素，共需要经过n-1次比对，第二次遍历时，最大的元素已经在列表的最后了，还有n-1个元素需要排序，要经过n-2次比较，所以一共需要n-1次遍历，到最后一次遍历时，最小的元素已经在自己的位置上了，不需要进行处理。

#### Code
```
def bubbleSort(alist:List):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]: 
                # temp = alist[i+1]
                # alist[i+1] = alist[i]
                # alist[i] = temp
                alist[i],alist[i+1] = alist[i+1],alist[i]   # Python 支持直接交换
```
### 分析
冒泡排序是效率最低的排序算法，在确定最终位置前必须交换元素，“多余”交换的代价很大，不过冒泡排序会遍历列表中未排序的部分，但是它的优势是不需要额外的储存开销，有如果在某一轮遍历中没有发生元素交换，就可以确定列表已经有序了。

总比对次数 $ =1+2+...+n-1=\frac{n^2-n}{2}$
比对的时间复杂度: $O(n^2)$

交换次数的时间复杂度: $O(n^2)$，每次交换包括3次赋值
- 最好的情况：本身已经有序，交换次数为0
- 最差的情况：每次比对都要交换，交换次数等于比对次数
- 平均情况：最差情况的一半

#### 改进后的Code
```
def shortbubbleSort(alist:List):
    exchange = True
    passnum = len(alist) - 1
    while exchange and passnum > 0:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]: 
                exchange = True
                alist[i],alist[i+1] = alist[i+1],alist[i]
        passnum = passnum - 1
```


### 选择排序
在冒泡排序的基础上做了改进，每次遍历只做一次交换，选择排序在每次遍历时寻找最大值，并且在遍历完之后把它放在正确位置上，和冒泡排序一样，第一次遍历后，最大的元素在列表末尾，依次类推，给n给元素排序需要经过n-1轮遍历。

比对次数时间复杂度：$O(n^2)$
交换次数时间复杂度：$O(n)$

#### Code
```
def selectionSort(alist:List):
    for i in range(len(alist)-1,0,-1):
        posMax = 0
        for loc in range(1,i+1):
            if alist[loc] > alist[posMax]:
                posMax = loc
        temp = alist[i]
        alist[i] = alist[posMax]
        alist[posMax] = temp
```