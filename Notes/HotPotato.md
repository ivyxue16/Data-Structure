# 4.2 队列的应用：热土豆问题（约瑟夫问题）

### 问题描述：
这是队列应用的经典问题，假设有N个小孩围成一个圈，传烫手的热土豆，鼓声停的时候，手中有土豆的小孩就要出列，游戏一直继续直到最后只剩下一个小孩。
![IMAGE](quiver-image-url/E08C80BF1FB70A62BE81918D6B24B839.jpg =378x289)

如果去掉鼓，改为传过固定人数，就成了”现代版“的约瑟夫问题。
传说犹太人反叛罗马人，落到困境，约瑟夫和39名人决定殉难，坐成一个圈，报数1-7，报到7的人由旁边的人杀死，结果约瑟夫给自己安排一个位置没被杀死。

### 算法：
用队列来实现，输入参加游戏的人名列表，以及传土豆次数num，最后返回最后剩下的人名。

游戏过程中，用队列存放参加游戏的人名，按照传递土豆方向从队首排到队尾，队首始终是持有土豆的人。
![IMAGE](quiver-image-url/583EF4466868D06D13BEDC65F559DA8A.jpg =504x234)

开始后只需要让队首的人出队，再加入队尾，经过num传递后，将队首的人从队列中移除，不再入队，重复这个过程，直到队列中只剩一个人。

*注：这个过程中，num可以大于参与游戏的人的个数，因为参与者围成一个圈。

### 代码：
```
def hot_potato(names:List[str], num:int) -> str:
    # put all children in the queue
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        
        queue.dequeue() # the child go out of the circle
    
    return queue.dequeue()


hot_potato(('Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'), 5)
# >>> 'Jane'
```