# 4.6 无序表抽象数据类型及Python实现
### 列表List
列表是一种数据项按照相对位置存放的数据集。
![IMAGE](quiver-image-url/68A0AB26EE56208A776826E741C4215A.jpg =269x162)


### 节点 Node
是指数据项只按照存放位置来索引，如第1个、第2个...假设表中不存在重复数据项
列表中的成员可以称为节点Nodes，如果每一个节点包含下一个节点的信息，则称这个列表为链接表Linked List
![node.png](quiver-image-url/B1DE0FD8D397596E56246636F78BE27E.png =78x19)


### 无序表 unordered list
例子：
考试分数的集合“54，26，93，17，77，31”；
用无序表表示[54,26,93,17,77,31]
![IMAGE](quiver-image-url/B9A3CF90FDD3054DB3F80FC2825E6FFC.jpg =342x160)

![IMAGE](quiver-image-url/AC11DA37DBFEE802CE95B2C7C6E24308.jpg =245x79)



### 无序表的操作：
**List()**:创建列表
**add(item)**:添加数据项到列表中，假设列表中原先不存在数据项item
**remove(item)**:从列表中移除item，列表被修改，item原先应该存在于列表中
**search(item)**:从列表中查找item，返回布尔类型值
**is_empty()**: 返回列表是否为空
**size()**: 返回列表包含的数据项个数
**append(item)**:添加一个数据项到表末尾，假设该数据项item原本不存在于列表内
**index(index)**:返回数据项在表中的位子
**insert(pos,item)**:将数据项item插入到pos位置上，假设item原先不存在于列表内，且列表有足够的数据项可以让item占据pos
**pop()**:从列表末端移除数据项，假设原列表至少有1个数据项
**pop(pos)**:移除位置为pos的数据项，假设原列表存在pos位置

### 无序表的实现：链表Linked List
列表数据结构要求保持数据项的前后相对位置，但是这种前后相对位置的保持，并不要求数据项依次存放在连的存储续空间内。数据项存放没有规则，但是如果在数据项之间建立链接指向，就可以保持它的先后相对位置。
第一个和最后一个数据项需要显式标记出来，一个是队首，一个是队尾，表面前后没有其他数据项了。如果想要访问链表中的所有节点，必须沿着第一个节点一个个遍历下去

![IMAGE](quiver-image-url/461D5BF161ADCC1EBE8D2DD1A563D78D.jpg =564x133)

链表实现的最基本元素是节点Node，每个节点至少包含2个信息：
- 数据项本身
- 指向的下一个节点的引用信息

注意：next为None的意义是没有下一个节点了

随着数据项的加入，无序表的head始终指向链表的第一个节点，无序mylist对象本身并不包含数据项，其中包含的head只是对某个节点Node的引用。判断空表的isEmpty()很容易实现。


```
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data = newData
    def setNext(self,newnext):
        self.next = newnext
```

### 无序表的链表实现
#### add(item)
实现**add**方法，由于无序表没有限定每个数据项之间的顺序，新的数据项可以加入到原表的任意位置，考虑到性能实现，应该加入最容易实现的位置。**表头**最容易加入，因为在表尾，需要要访问整条链上的所有数据项，都必须从表头head开始沿着next链接逐个向后查找，而加入表头，只需要将head指向新加入的数据项即可。

![IMAGE](quiver-image-url/B9073C0CB6AC10A3A7009D13390F294A.jpg =441x133)

注：链接的次序很重要！
先把新加入的数据项指向原来的表头(指向的数据)，再把原来的表头指向新加入的数据。

错误的顺序：
![IMAGE](quiver-image-url/F693A7AD086790BC2618486D4BF684B1.jpg =458x165)

```
def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
```
#### **size**: 从链表头head开始遍历到表尾同时用变量累加经过的节点个数。
```
def size(self):
        # O(n)
        current = self.head
        count = 0 
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
```

#### search: 寻找列表中是否存在某个数据项，返回布尔类型值
```
def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() != item:
                current = current.getNext()
            else:
                found = True
        return found
```
#### **remove**(item): 删除列表中为item的数据项

**技巧**：
用**两个变量**对列表进行索引，current和previous进行索引。

![IMAGE](quiver-image-url/1F9F2AAA4FE33C2AF5007D2E7E6FEFFB.jpg =545x324)

current为当前匹配数据项的节点，需要把current的前一个节点的next指向current指向的下一个节点，在search current的同时，维护前一个(previous)节点的引用。
![IMAGE](quiver-image-url/54BA4AC019F8E8994F352AD11D3D6645.jpg =521x138)



**逻辑：**
找到item后，current指向item节点，previous指向前一个节点。

![IMAGE](quiver-image-url/61451186A612E80D014989A32DF72593.jpg =512x113)

需要分为2种情况讨论：
- current是第一个节点
- current是处于链条当中的节点


```
def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData != item:
                previous = current
                current = current.getNext()
            else:
                found = True
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
```