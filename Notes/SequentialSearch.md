# 7.1 顺序查找Sequential Search

### 顺序查找
如果数据保存在列表中，则称数据具有线性或者顺序的关系，在Python中，数据项的存储位置称为下标(index)，这些下标都是有序的整数。通过下标，我们可以按照顺序来访问和查找数据项，这种查找方式称作为“顺序查找”。

要确定表中是否存在需要查找的数据项，首先从表中的第1个数据项开始，按照下标增长的顺序，逐个比对数据项，如果到最后一个都没有发现要寻找的数据项，则查找失败
![IMAGE](quiver-image-url/6ABB6B81171F6F2405990E570883BCF0.jpg =424x90)

基本计算步骤：进行数据项的比对，当前数据项是否等于要查找的数据项，总比对次数决定了算法的复杂度。

### 数据项未排序
在顺序算法中，为了保证讨论的一般情况，假定数据没有按值排列顺序，而是随机放置在表中的各个位置，即数据项出现在表中的任意位置的概率相同。

#### 顺序查找无序表Code
```
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
print(sequentialSearch(testlist,42))
```

#### 算法复杂度：$O(n)$
|Case|Best case|Worst case|Average case|
|:-----:|:-----:|:-----:|:-----:|
|item is present|1|n|n/2|
|item is not present|n|n|n|

### 数据项排序之后
如果是排过序的数据项，顺序查找
![IMAGE](quiver-image-url/500CE4141E6CC5022665715ED187FC50.jpg =441x90)

如果数据在列表中，比对过程与无序表相同，如果数据项不在表中，比对可以提前结束。

#### 顺序查找有序表Code
```
def orderedSequentialSearch(searchList:List, item):
    pos = 0
    found = False
    stop = False

    while pos < len(searchList) and not found and not stop:
        if searchList[pos] == item:
            return True
        else:
            if searchList[pos] > item:
                stop = True
                return False
            else:
                pos += 1
    return found

print(orderedSequentialSearch(testlist,42))
print(sequentialSearch(testlist,18))
```

#### 算法复杂度：$O(n)$
|Case|Best case|Worst case|Average case|
|:-----:|:-----:|:-----:|:-----:|
|item is present|1|n|n/2|
|item is not present|1|n|n/2|

实际上只有在数据项不在列表中的情况下可以提前结束查找，但是并没有改变数量级。

