# 7.3 排序算法

## 总结

|排序算法|平均时间复杂度|最好情况|最差情况|空间复杂度|排序方式|稳定性|
|-----|-----|-----|-----|-----|-----|-----|
|冒泡排序|$O(n^2)$|$O(n)$|$O(n^2)$|$O(1)$|In-place|稳定|
|选择排序|$O(n^2)$|$O(n^2)$|$O(n^2)$|$O(1)$|In-place|不稳定|
|插入排序|$O(n^2)$|$O(n)$|$O(n^2)$|$O(1)$|In-place|稳定|
|希尔排序|$O(nlogn)$|$O(n log^2n)$|$O(n log^2n)$|$O(1)$|In-place|不稳定|
|归并排序|$O(nlogn)$|$O(n logn)$|$O(n logn)$|$O(n)$|Out-place|稳定|
|快速排序|$O(nlogn)$|$O(n logn)$|$O(n^2)$|$O(logn)$|In-place|不稳定|
|堆排序|$O(nlogn)$|$O(n logn)$|$O(n logn)$|$O(1)$|In-place|不稳定|


### 冒泡排序 Bubble
每次循环中比较相邻的元素，将不合顺序的交换，把最大值放在列表的最后。如果列表中有n个元素，共需要经过n-1次比对，第二次遍历时，最大的元素已经在列表的最后了，还有n-1个元素需要排序，要经过n-2次比较，所以一共需要n-1次遍历，到最后一次遍历时，最小的元素已经在自己的位置上了，不需要进行处理。
![IMAGE](quiver-image-url/90FA80CA959396D3BB3E380BBB3467AE.jpg =376x315)

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


### 选择排序 Selection
在冒泡排序的基础上做了改进，每次遍历只做一次交换，选择排序在每次遍历时寻找最大值，并且在遍历完之后把它放在正确位置上，和冒泡排序一样，第一次遍历后，最大的元素在列表末尾，依次类推，给n给元素排序需要经过n-1轮遍历。
![IMAGE](quiver-image-url/6E71153300307D329B3C62581A92C71C.jpg =391x491)

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

### 插入排序 Insertion

在列表的一端维护一个排序后的子列表，总共需要n-1次遍历，在每一次遍历中新元素都与之前的数进行比对，插入到有序的子列表中。在有序子列表中，比它大的元素向右移动，遇到比它小或者到达列表尽头时就可以插入当前元素

![IMAGE](quiver-image-url/1A3F289CA1504ED014073366EADE60B3.jpg =444x433)

比对次数时间复杂度：
- 最差情况：$O(n^2)$
- 最好情况：$O(n)$


#### Code
```
def insertionSort(alist:List):
    for i in range(1,len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue

```

![IMAGE](quiver-image-url/0F5EB7F2E840991C6750769EA4E285DD.jpg =497x383)

### 谢尔排序 Shell 
假设一群人随机站好，目标是按照身高从小到大排好，让这些人按照1-n报数，报数为同样数字的人为一组，在每一组中进行排序，所有组都排序完成后，再按照1-k进行报数，重复上述操作，其中k<n，直到最后一组只有1个人，进行排序后就能得到完整的排序后的列表。

也叫作“递减增量排序”，在插入排序上做了改进，将列表分为数个子列表，对每个子列表应用插入排序，谢尔排序切分列表不是连续切分，而是使用增量i（选取所有间隔为i的元素组成子列表）
虽然谢尔排序在最后一步需要做完整的插入排序，但是由于列表已经做过预处理，所以最后一步非常高效。


时间复杂度：
- 介于$O(n)和O(n^2)之间$
- 如果采用$2^k-1$为增量，谢尔排序的复杂度为$O(n^\frac{3}{2})$

![IMAGE](quiver-image-url/BF6920B8C70D864DEF16259C14918F39.jpg =463x497)


#### Code
```
def shellSort(alist:List):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startposition in range(sublistCount):
            gapInsertionSort(alist,startposition,sublistCount)
        print("After increments of size ", sublistCount, " The list is ",alist)
        sublistCount = sublistCount // 2

def gapInsertionSort(alist:List,start:int,gap:int):
    for i in range(start + gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue
```

### 归并排序 Merge
使用分治策略的一种排序，是一种递归算法，将列表一分为二。如果列表为空或者只有一个元素，那么它就是有序的，如果不止一个元素就将列表一分为二，并对两部分都递归调用归并操作，归并时每次都从列表中找到最小的值放入初始列表。

分析：考虑拆分和归并两个部分
- 拆分：列表每次一分为二，时间复杂度为$O(logn)$
- 归并：列表中的每个元素都会被处理，每一个需要n次操作
- 一共是$nlogn$次操作，时间复杂度为$O(nlogn)$，

![IMAGE](quiver-image-url/8B02C294BD93929C32C0A3BA3BDB19C0.jpg =525x659)

#### Code
```
def mergeSort(alist:List):
    print('Splitting ',alist)
    if len(alist) > 1:
        mid = len(alist) // 2 
        leftlist = alist[:mid]
        rightlist = alist[mid:]

        mergeSort(leftlist)
        mergeSort(rightlist)

        i = 0
        j = 0
        k = 0
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k] = leftlist[i]
                i = i + 1
            else:
                alist[k] = rightlist[j]
                j = j + 1
            k = k + 1
        
        while i < len(leftlist):
            alist[k] = leftlist[i]
            i = i + 1
            k = k + 1
        
        while j < len(rightlist):
            alist[k] = rightlist[j]
            j = j + 1
            k = k + 1
        
        print('Merging ', alist)
```

### 快速排序 Quick
快速排序也采用了分治策略，但不会使用额外的存储空间，代价是列表不会一分为二。快速排序首先选出一个基准值，一般为第一个元素，找到它在排序后的列表中的正确位置，第一次排序中让所有比它小的在它左边，比它大的在它右边。在分区时会使用两个指针，分别位于列表剩余元素的开头和末尾。leftmark在找到比基准值大的数字停下，rightmark在找到比基准值小的数字停下，此时交换leftmark和rightmark所指向的数字，然后leftmark再向右出发，直到找到比基准值大的数字，rightmark再向左出发，直到找到比基准值小的数字。当最终leftmark和rightmark交错时(rightmark < leftmark),整个列表的元素都已经完成遍历，而rightmark所在位置即为分割点，此时交换rightmark和基准值的位置即可。

![IMAGE](quiver-image-url/EA5EDF2E8D8F595BA2A4371199FEB7BC.jpg =412x498)

分析：
对于长度为n的列表
- 如果分区操作总是在列表的中部，就会切分$logn$次，为了找到分割点，n个元素都要和基准值比较，所以时间复杂度为$O(nlogn)$
- 如果分区操作总是在列表的某一段，那么切分就不均匀，时间复杂度也变为$O(n^2)$
可以使用首个，中间数，末尾三个数字取中法来避免切分不均匀。


#### Code
```
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    '''
    Use recursion to sort list with smaller list
    '''
    if first < last:
        splitPoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitPoint-1)
        quickSortHelper(alist,splitPoint+1,last)

def partition(alist,first,last):
    pivotValue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while alist[leftmark] <= pivotValue and leftmark <= rightmark:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotValue and leftmark <= rightmark:
            rightmark = rightmark - 1
        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
        
    alist[first], alist[rightmark] = alist[rightmark],alist[first]
    return rightmark
```

