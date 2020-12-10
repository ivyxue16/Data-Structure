# 4.7 有序表OrderedList抽象数据类型及其Python实现
### 有序表OrderedList定义
有序表示数据项按照某种可比性质(整数大小、字母表先后顺序)来决定在列表中的位置
![IMAGE](quiver-image-url/41D9E036D8375CD0EEDDBCE732BE83D1.jpg =512x41)
### 有序表OrderedList操作
**OrderedList()**: 创建一个空的列表
**add(item)**:在表中添加一个数据项，保持整体顺序，此项原本不存在，与无序表不同
**remove(item)**:从有序表中移除一个数据项，此项应该存在，有序表被修改
**search(item)**:在有序表中查找数据项，返回是否存在
**isEmpty()**:是否空表
**size()**:返回表中数据项的个数
**index(item)**:返回数据项在表中的位置，此项应存在
**pop()**:移除并返回有序表中最后一项，表中应至少存在一项
**poo(pos)**:移除并返回有序表中指定位置的数据项，此位置应该存在


### 有序表OrderedList实现
#### 表头head
采用链表，Node定义相同，也设置一个head来保持链表的表头，与无序表相似
```
class OrderedList(UnorderedList):
    def __init__(self):
        self.head = None
```
#### isEmpty/size/remove与节点的次序无关
实现与无序表UnorderedList相同

#### search
![IMAGE](quiver-image-url/F77FC5ECDF31DA9DD6D11F2DBDADE8C9.jpg =512x136)
有序表实现search方法，与无序表不同，有序表中的数据项有序排列，可以节省不存在数据项的查找时间，一旦当前节点的数据项大于所要查找的数据项，则说明链表中不存在要查找的数据项，可以直接返回False


```
def search(self,item):
    current = self.head
    while current is not None:
        if current.getData == item:
            return True
        else:
            if current.getData > item:
                return False
    current = current.getNext()
    return False
```
#### add(item)
由于涉及到的插入位置是当前节点之前，而链表无法得到“前驱”节点的引用，所以与remove方法类似，也需要引入两个索引，previous和current，一旦找到首个比item要大的数字，previous就能派上用场了。  

![IMAGE](quiver-image-url/FD63C79F514E52A3874A9D961EF1E2C3.jpg =512x202)


```
def add(self,item):
    previous = None
    current = self.head
    stop = False
    while current is not None and not stop:
        if current.value > item:
            stop = True
        else:
            previous = current
            current = current.getNext()
    temp = Node(item)
    if previous == None:
        temp.setNext(self.head)
        self.head = temp
    else:
        temp.setNext(current.getNext())
        previous.setNext(temp)
```

### 链表操作的算法分析
isEmpty的时间复杂度：O(1)，直接判断表头是否为None
size的时间复杂度：O(n)，需要对于遍历表中每一个数据项
add的时间复杂度：O(n)，有序表必须保证加入的数据项添加在合适的位置，以维护整个链表的有序性；无序表仅插入到表头，所以是O(1)
search的时间复杂度：O(n)，平均查找$\frac{n}{2}$次
remove的时间复杂度：O(n)，需要对于遍历表中每一个数据项，平均查找$\frac{n}{2}$次


|操作实现|无序表|有序表|
|:-----:|:-----:|:-----:|
|isEmpty|O(1)|O(1)|
|size|O(n)|O(n)|
|add|O(1)|O(n)|
|remove|O(n)|O(n)|
|search|O(n)|O(n)|

链表实现的List和Python内置的列表数据类型在相同方法的实现上的时间复杂度不同
