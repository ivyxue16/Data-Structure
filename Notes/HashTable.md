# 8.1 散列 Hash Table
### 定义 
散列表(哈希表）是元素集合，表中的每个位置称为槽，可以存储一个元素，初始情况中槽中没有元素，用None来表示。散列函数将散列表中的元素和其所属位置一一对应起来，散列函数可以使用取余函数，用一个元素除以散列表的大小，并将余数作为散列值。
占用率称为载荷因子，记作$\lambda$, $$\lambda = \frac{元素个数}{散列表大小}$$
搜索目标元素时，仅需使用散列函数计算出该元素的槽编号，并查看对应的槽中是否有值，计算散列值找到相依位置所需时间是固定的，搜索算法的时间复杂度是O(1)。
如果两个元素的散列值相同，就会产生冲突(碰撞)。

### 散列函数
#### 完美散列函数
定义：给定元素集合，能够把每个元素映射到不同的槽中。
方法：
- **增大散列表**，如果元素少则可以做到，但元素多时就会浪费内存空间。
- **折叠法**：将元素切成等长的几个部分，将这些部分相加再取余数。
  - 436-555-4601可以分为43，65，55，46，01，数字相加后得到210，假设有11个槽，取余得到1。即436-555-4601会被映射到1号槽中。
  - 也可以在加总之前先反转数字，43，56，55，64，01，加总为219，219%11 = 10
- **平方取中法**：先将元素平方，再取中间几位数取余
  - $44^2 = 1936$，中间数为93。继续取余，得到5(93%11)。
- 基于字符的元素，把字符转化为序列值，将序列值相加，采用取余法得到散列值。

#### 处理冲突

- **开放定址法** 
  - 从散列值开始，向后找到一个空槽，放入元素。这种方法被称为线性探测。但会造成聚集现象，此时可以对间隔变为+3，或者不固定的间隔(1,3,5,7,9)，让元素分布在所有槽中。如果使用+3，应该使散列表中所有元素都能遍历到，不能呈现周期性。
- **再散列**
  - 求出散列值后通过散列函数计算出新的散列值。rehash(pos) = (pos+1)%sizeoftable
- **平方探测**
  - 通过再散列函数递增散列值，如果第一个散列值是h，后续的散列值就是h+1,h+4,h+9,h+16，跨步为一系列完全平方数。
- **链接法**
  - 允许槽中有多个元素，每个槽有指向元素的集合（链表）的引用。
  - 搜索时需要进行两次搜索，第一次计算出元素的散列值，查找到对应的槽，槽里有多个元素，需要再搜索一次。

### 字典
给定一个键，可以很快找到关联的值，散列搜索的时间复杂度为O(1)

### 创建HashTable类
包含的方法：
- 初始化为两个列表，分别包含键和元素
- hashfunction(key): 把值作为输入，得到对应的散列值，通过取余法。如果遇到冲突，则采取+1的线性探测法
- rehash(oldhash)：把散列值作为输入，得到新的散列值
- put(key,data)：添加一对新的键值对
- get(key):输入位置，得到对应的数据

### 算法分析
在最好情况下，散列搜索算法的时间复杂度为$O(1)$，但实际会发生冲突，此时载荷因子$\lambda$就显得很重要。
采用**线性探测策略的开放定址法**，搜索成功的平均比较次数为$$\frac{1}{2}(1+\frac{1}{1-\lambda})$$
搜索失败的平均比较次数为$$\frac{1}{2}(1+(\frac{1}{1-\lambda})^2)$$
采用**链接法**，搜索成功的平均比较次数为$$1+\frac{\lambda}{2}$$
搜索失败的平均比较次数为$$\lambda$$

**Code**
```
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        return key % self.size

    def rehash(self,oldhash):
        return (oldhash + 1) % self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else: 
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data # replace
                    
    def get(self,key):
        startslot = self.hashfunction(key)
        position = startslot
        data = None
        while self.slots[position] != None:
            if self.slots[startslot] == key:
                return self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    break
        return data
```

