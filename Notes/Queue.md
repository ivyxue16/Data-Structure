# 4.1 队列Queue抽象数据类型及Python实现
### 队列的定义
队列是有次序的数据集合，新数据的添加总发生在一端(尾端Rear),现存数据的移除发生在另一端(首端)。当数据加入时，首先出现在队尾，随着队列中的数据逐渐移除时，它逐渐接近队首。

**次序出现的原则**：FIFO(First-In-First-Out)
队列仅有一个出口和入口，数据项不允许直接插入队列中，也不允许从中间移除数据项。

**例子**：
- 打印队列：一台打印机面向多个用户/程序提供服务。当打印的速度比打印请求提交的速度要慢很多，有任务正在打印时，后来的打印请求就要排成队列，以FIFO的形式等待被处理。
- 进程调度：操作系统核心采用多个队列来对系统中同时运行的进程进行调度。进程数远远多于CPU核心数。调度原则综合FIFO及“资源充分利用”这两个出发点。
- 键盘缓冲：键入的速度大于显示的速度，需要有一个缓冲区暂存字符，保证字符输入顺序和显示顺序一致。

### 抽象数据结构Queue
Queue是个有次序的数据集合，数据项仅添加到"尾端Rear"，而且仅从"首端Front"移除。Queue具有FIFO的操作次序。

抽象数据类型Stack定义为如下操作：

**Queue()**: 创建一个空栈，不包括任何数据项
**enqueue(item)**: 将item加入队尾，无返回值
**dequeue()**: 将队首移除数据项，并返回，栈被修改
**isEmpty()**: 返回队列是否为空队列
**size()**: 返回队列中有多少个数据项

### **Stack操作例子**
|Stack Operation|Stack Contents|Return Value|
|:-----|:-----|:-----|
|s = Queue()|[]|Queue Object|
|s.isEmpty()|[]|True|
|s.enqueue(4)|[4]||
|s.enqueue('dog')|['dog',4]||
|s.enqueue(True)|[True,'dog',4]||
|s.size()|[True,'dog',4]|3|
|s.isEmpty()|[True,'dog',4]|False|
|s.enqueue(8.4)|[8.4,True,'dog',4]||
|s.dequeue()|[8.4,True,'dog']|4|
|s.dequeue()|[8.4, True]|'dog'|
|s.size()|[8.4, True]|2|

Python中ADT Queue实现方法：
- 将ADT Queue实现为Python的一个Class
- 将ADT Queue的操作实现为Class的方法
- 由于Queue是一个数据集，所以可采用Python的原生数据集来实现，我们选用最常用的数据集List来实现

细节：Queue两端对应list设置
  - 可以将List的任意一端(index = 0 或者 -1) 设置为队尾，我们采用List的末端(index = -1)作为队首，这样可以用list的pop来实现
  - 其enqueue的复杂度为O(n)，dequeue()的复杂度为O(1)，首尾倒过来复杂度也倒过来




