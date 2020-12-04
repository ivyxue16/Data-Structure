# 3.2 线性结构Linear Structure — Stack 
线性结构是有序数据项的集合，每个数据都有唯一的前驱和后继，除了第一个和最后一个。新的数据被加入到数据集中时，只会加入到原有某个数据项之前或之后。线性结构总有两端，不同的是数据增减的方式。

线性结构包括：栈Stack，队列Queue， 双端队列Deque，列表List。
共同点：数据只存在先后的次序关系。


### 1. 栈Stack
一种有序的数据项集合，数据的加入和移除只发生在其中一端。这一端叫作“顶top”，另一端叫作“底base”。
例如：盘子、书堆、托盘

距离栈底越近的数据留在栈中的时间越长，最新加入的数据会被最先移除，这种次序被称为Last In First Out (LIFO)，这是基于数据项保存时间的次序，时间越短的离栈顶越近，而时间越长的离栈顶越近。

栈的特性：反转次序
例如：浏览器的后退back按钮、word文档的undo按钮，最先撤销最近的操作

抽象数据类型Stack定义为如下操作：

**Stack()**: 创建一个空栈，不包括任何数据项
**push(item)**: 将item加入栈顶，无返回值
**pop()**: 将栈顶数据项移除，并返回，栈被修改
**peek()**:  “窥视”栈顶数据项，返回栈顶的数据项但不移除，栈不被修改
**isEmpty()**: 返回栈是否为空栈
**size()**: 返回栈中有多少个数据项

**Stack操作例子**
|Stack Operation|Stack Contents|Return Value|
|:-----|:-----|:-----|
|s = Stack()|[]|Stack Object|
|s.isEmpty()|[]|True|
|s.push(4)|[4]||
|s.push('dog')|[4,'dog']||
|s.peek()|[4,'dog']|'dog'|
|s.push(True)|[4,'dog',True]||
|s.size()|[4,'dog',True]|3|
|s.isEmpty()|[4,'dog',True]|False|
|s.push(8.4)|[4,'dog',True,8.4]||
|s.pop()|[4,'dog',True]|8.4|
|s.pop()|[4,'dog']|True|
|s.size()|[4,'dog']|2|

Python中ADT Stack实现方法：
- 将ADT Stack实现为Python的一个Class
- 将ADT Stack的操作实现为Class的方法
- 由于Stack是一个数据集，所以可采用Python的原生数据集来实现，我们选用最常用的数据集List来实现

细节：Stack两端对应list设置
  - 可以将List的任意一端(index = 0 或者 -1) 设置为栈顶，我们采用List的末端(index = -1)作为栈顶，这样可以用list的append和pop来实现
  - 如果使用栈顶首端的版本(index = 0)，其push/pop的复杂度为O(n)，而栈顶尾端实现的push/pop复杂度为O(1)