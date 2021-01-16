# 7.2 二分查找 Binary Search

列表已经是值排序后的结果，二分查找从列表中间开始比对
- 如果列表中间的值匹配查找项，查找结束
- 如果不匹配，有两种情况：
  - 列表中间项比查找项大，查找项只可能出现在前半部分
  - 列表中间项比查找项小，查找项只可能出现在后半部分
- 无论如何都会将比对范围缩小到原来的$\frac{n}{2}$
![IMAGE](quiver-image-url/AD31B8B23487BDB2122EF86F9C16951F.jpg =384x117)

二分查找实际上体现了解决问题的典型策略：分而治之。将问题分成更小规模的部分，通过解决每一个更小规模的问题，将结果汇总得到原问题的解

### Code
```
def binarySearch(alist:List,item:int) -> bool:
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found: # not found must be included
        mid = (first + last) // 2 
        if alist[mid] == item:
            return True
        else:
            if alist[mid] < item:  
                first = mid + 1 
            else: 
                last = mid  - 1
    return found
    
testlist = [1,2,32,8,17,19,42,13,0]
print(binarySearch(testlist,41))
print(binarySearch(testlist,42))
```

#### 使用递归
```
def binarySearchRec(alist:List,item:int) -> bool:
    
    if len(alist) == 0:
        return False
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found: # not found must be included
        mid = (first + last) // 2 
        if alist[mid] == item:
            return True
        else:
            if alist[mid] < item:  
                return binarySearchRec(alist[mid+1:],item)
            else: 
                return binarySearchRec(alist[:mid],item)
    return found

testlist = [1,2,32,8,17,19,42,13,0]
print(binarySearchRec(testlist,41))
print(binarySearchRec(testlist,42))
```

### 算法分析 复杂度: $O(log\ n)$
|Comparison|Approximate Number of Items Left|
|:-----:|:-----:|
|1|$n/2$|
|2|$n/4$|
|…|$n/8$|
|i|$n/2^i$|

当比对次数足够多之后，比对范围就会缩小为1个数据项，无论是否匹配数据项，查找都会结束，解方程：
$$\frac{n}{2^i} = 1$$
得到$i = log_2(n)$

### 进一步的考虑
虽然二分查找在时间复杂度上优于顺序查找，但也要考虑到对数据项进行排序的开销，如果一次排序可以用于多次查找，排序的开销就可以摊薄，但如果数据集经常变动，查找次数相对较少，那么直接用无序表加上顺序查找更经济。还是要结合实际情况，不能只看时间复杂度。