# 5.6 递归调用：汉诺塔 Tower of Hanoi

### 汉诺塔问题介绍
在1883年由法国数学家Edouard Lucas提出，从印度传说得来
![IMAGE](quiver-image-url/8A1CF6B4CA3D10E29BB5595A5B450807.jpg =320x125)
有3根柱子，把一个套有64根柱子的盘片从一根搬到另一个上，遵循两个原则：
- 一次搬动一个盘片
- 大盘子不能叠在小盘子上

![IMAGE](quiver-image-url/F3E22A6FE7073873E54BC25112518362.jpg =101x186)

由大到小的盘片移动的次数依次为
$1、2、……、2^{n-2}、2^{n-1}$
n个盘片总共需要移动$2^{n}-1$次才能从最左端的柱子移动到最右端的柱子上

### 时间复杂度
$O(2^n)$

### 算法分析
- 假设第一根柱子起初有5个盘子，如果我们知道如何把上面4个盘子移动到第2根柱子上，那么轻易地就能将最底下的盘子移动到第3根柱子上。再把上面4个盘子从中间柱子移动到第3根柱子上。
- 但是如果不知道怎么移动4个盘子，该怎么办？
如果我们知道如何把上面3个盘子移动到第3根柱子上，我们就能把第4个盘子移动到中间柱上，然后再把3个盘子移动到中间柱上。
- 但是如果我们不知道怎么移动3个盘子，该怎么办？
如果我们知道如何移动2个盘子到中间柱，就能把第3个盘子移动到第3根柱子上，最后把2个盘子移动过来。
- 但是如果我们还是不知道怎么移动2个盘子，该怎么办？
我们显然知道怎么移动1个盘子到第三根柱子上，这就是base case

### 算法概述
将高度为height的一叠盘子由中间柱移动到终点柱子：
- 借助终点柱子，将高度为$height - 1 $的柱子移动到中间柱
- 移动最下面的盘子到终点柱子
- 借助起点柱子，将高度为$height - 1 $的柱子移动到终点柱子
- 基本情况：只有一个盘子，直接将这个盘子移动到终点柱

### 满足递归三定律
- 基本结束条件：盘片个数为0
- 减小规模：每次递归时盘片层数-1
- 调用自身：在每次递归时调用高度减小1的盘片移动


### Code
```
def moveTower(height,fromPole,withPole,toPole):
  if height >= 1:
      moveTower(height-1,fromPole,toPole,withPole)
      moveDisk(height,fromPole,toPole)
      moveTower(height-1,withPole,fromPole,toPole)

def moveDisk(disk,fromPole,toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")
    
moveTower(3,"#1","#2","#3")
```

### 递归执行代码拆解
```
moveTower(height=3,fromPole="#1",withPole="#2",toPole="#3")
  if height=3 >= 1:
    moveTower(2,fromPole='#1',toPole='#3',withPole='#2')
      moveTower(2,fromPole='#1',withPole='#3',toPole='#2')
      if height=2 >= 1:
        moveTower(1,fromPole='#1',toPole='#2',withPole='#3')
    
          moveTower(1,fromPole='#1',withPole='#2',toPole='#3')
            if height >= 1:
              moveTower(0,fromPole,toPole,withPole)
              moveDisk(1,fromPole='#1',toPole='#3')
              moveTower(0,withPole,fromPole,toPole)
              
        moveDisk(2,fromPole='#1',toPole='#2')
        
        moveTower(1,withPole='#3',fromPole='#1',toPole='#2')
          moveTower(1,fromPole='#3',withPole='#1',toPole='#2')
            if height >= 1:
              moveTower(0,fromPole,toPole,withPole)
              moveDisk(1,fromPole='#3',toPole='#2')
              moveTower(0,withPole,fromPole,toPole)
      
    
    moveDisk(3,fromPole'#1',toPole'#3')
    
    moveTower(2,withPole='#2',fromPole='#1',toPole='#3')
      moveTower(2,fromPole='#2',withPole='#1',toPole='#3')
      if height=2 >= 1:
          moveTower(1,fromPole='#2',toPole='#3',withPole='#1')
              moveTower(1,fromPole='#2',withPole='#3',toPole='#1')
                if height >= 1:
                moveTower(0,fromPole'#2',toPole'#1',withPole'#3')
                moveDisk(1,fromPole'#2',toPole='#1')
                moveTower(0,withPole,fromPole,toPole)
                
      moveDisk(2,fromPole='#2',toPole='#3')
      
      moveTower(1,withPole='#1',fromPole='#2',toPole='#3')
        moveTower(1,fromPole='#1',withPole='#2',toPole='#3')
          if height >= 1:
          moveTower(0,fromPole,toPole,withPole)
          moveDisk(1,fromPole='#1',toPole='#3')
          moveTower(0,withPole='#2',fromPole='#1',toPole='#3')

# 第2层
moveTower(2,fromPole='#1',withPole='#3',toPole='#2')
  if height=2 >= 1:
      moveTower(1,fromPole='#1',toPole='#2',withPole='#3')
  
        moveTower(1,fromPole='#1',withPole='#2',toPole='#3')
          if height >= 1:
            moveTower(0,fromPole,toPole,withPole)
            moveDisk(1,fromPole='#1',toPole='#3')
            moveTower(0,withPole,fromPole,toPole)
            
      moveDisk(2,fromPole='#1',toPole='#2')
      
      moveTower(1,withPole='#3',fromPole='#1',toPole='#2')
        moveTower(1,fromPole='#3',withPole='#1',toPole='#2')
          if height >= 1:
            moveTower(0,fromPole,toPole,withPole)
            moveDisk(1,fromPole='#3',toPole='#2')
            moveTower(0,withPole,fromPole,toPole)


moveTower(2,fromPole='#2',withPole='#1',toPole='#3')
  if height=2 >= 1:
      moveTower(1,fromPole='#2',toPole='#3',withPole='#1')
          moveTower(1,fromPole='#2',withPole='#3',toPole='#1')
            if height >= 1:
            moveTower(0,fromPole'#2',toPole'#1',withPole'#3')
            moveDisk(1,fromPole'#2',toPole='#1')
            moveTower(0,withPole,fromPole,toPole)
        
        
      moveDisk(2,fromPole='#2',toPole='#3')
      moveTower(1,withPole='#1',fromPole='#2',toPole='#3')
        moveTower(1,fromPole='#1',withPole='#2',toPole='#3')
          if height >= 1:
          moveTower(0,fromPole,toPole,withPole)
          moveDisk(1,fromPole='#1',toPole='#3')
          moveTower(0,withPole='#2',fromPole='#1',toPole='#3')


# 最底层
moveTower(2,fromPole='#1',withPole='#3',toPole='#2')
  moveTower(1,fromPole='#1',withPole='#2',toPole='#3')
    if height >= 1:
      moveTower(0,fromPole,toPole,withPole)
      moveDisk(1,fromPole='#1',toPole='#3')
      moveTower(0,withPole,fromPole,toPole)
  
  moveTower(1,fromPole='#3',withPole='#1',toPole='#2')
    if height >= 1:
      moveTower(0,fromPole,toPole,withPole)
      moveDisk(1,fromPole='#3',toPole='#2')
      moveTower(0,withPole,fromPole,toPole)



moveTower(2,fromPole='#2',withPole='#1',toPole='#3')
  moveTower(1,fromPole='#2',withPole='#3',toPole='#1')
    if height >= 1:
    moveTower(0,fromPole'#2',toPole'#1',withPole'#3')
    moveDisk(1,fromPole'#2',toPole='#1')
    moveTower(0,withPole,fromPole,toPole)
  
  moveTower(1,fromPole='#1',withPole='#2',toPole='#3')
    if height >= 1:
    moveTower(0,fromPole,toPole,withPole)
    moveDisk(1,fromPole='#1',toPole='#3')
    moveTower(0,withPole='#2',fromPole='#1',toPole='#3')
 ``` 