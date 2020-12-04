# 研究列表list和字典dict的各种操作的大O数量级

### 1. 对比list和dict的不同操作
|类型|list|dict|
|:-----:|:-----:|:-----:|
|索引| 自然数i|不可变类型值key |
|添加|append、extend、insert|b[k]=v|
|删除|pop、remove|pop|
|更新|a[i]=v|b[k]=v|
|正查|a[i]、a[i:j]|b[k]、copy|
|反查|index(v)、count(v)|无|
|其他|reverse、sort|has_key、update|

### 2. list 列表数据类型常用操作性能
1. 按索引取值、赋值(a[i]=v、v=a[i])
  由于列表的随机访问特性，这两个操作的执行时间与列表大小无关，都为O(1)
2. 列表增长，可以选择.append(),__add__()"+"
  lst.append(v),执行时间为O(1)
  lst= lst+ [v], 执行时间为O(n+k),n为lst的长度，k为被加的列表长度

### 3. 四种生成前n个整数列表的方法
使用timeit模块对函数计时，创建一个Timer对象，指定需要反复运行的执行语句，以及只需要运行一次的“安装语句”，然后调用这个对象的timeit方法，其中可以指定反复运行多少次

**1. 用循环连接列表(+)**
```
def test1():
  l = []
  for i in range(1000):
  l = l + [i]
```

**2. 用append()方法**
```
def test2():
  l = []
  for i in range(1000):
  l.append(i)
```

**3. 列表推导式**
```
def test3():
  l = [i for i in range(1000)]
```

**4. range函数调用转成列表**
```
def test4():
  l = list(range(1000))
```
**测试运行时间**
```
from timeit import Timer
t1 = Timer("test1()","from __main__ import test1")
print("concat %f second\n" %t1.timeit(number=1000))

t2 = Timer("test2()","from __main__ import test2")
print("append %f second\n" %t2.timeit(number=1000))

t3 = Timer("test3()","from __main__ import test3")
print("comprehension %f second\n" %t3.timeit(number=1000))

t4 = Timer("test4()","from __main__ import test4")
print("list range %f second\n" %t4.timeit(number=1000))
```

**运行结果**
****************
concat 0.793334 second
append 0.058168 second
comprehension 0.028503 second
list range 0.011573 second
****************
**concat最慢，list range最快，comprehension是append的2倍**

### 4. List基本操作的大O数量级
|Operation|Big-O Efficiency|
|:-----:|:-----:|
|index[]|O(1)|
|index assignment|O(1)|
|append|O(1)|
|pop()|O(1)|
|pop(i)|O(n)|
|insert(i,item)|O(n)|
|del operator|O(n)|
|iteration|O(n)|
|contains (in)|O(n)|
|get slice [x:y]|O(k)|
|del slice|O(n)|
|set slice|O(n+k)|
|reverse|O(n)|
|concatenate|O(k)|
|sort|O(n log n)|
|multiply|O(nk)|

**list.pop的计时实验**
pop()从列表末尾移除元素，O(1)
pop()从列表中部移除元素，O(n)
pop()的时间不随list大小变化，pop(0)的时间随着list变大而变长
原因在于Python选择的实现方法中,从中部移除元素需要把移除元素后所有的元素全部向前挪位复制一遍，但这个操作可以让按索引取值和赋值的操作很快，达到O(1)


### 5.Dict基本操作的大O数量级
字典根据关键码(key)找到数据项，而列表是根据位置(index)
|Operation|Big-O Efficiency|
|:-----:|:-----:|
|copy|O(n)|
|get item|O(1)|
|set item|O(1)|
|delete item|O(1)|
|contain (in)|O(1)|
|iteration|O(n)|
