# 5.4 递归可视化：分形树 Fractal Tree
### 利用递归画五角星
![IMAGE](quiver-image-url/EA0F57E0DD35AE4B14BF232ACAEE1F19.jpg =239x225)
```
import turtle
t = turtle.Turtle()

t.pencolor('red')
t.pensize(3)
for i in range(5):
    t.forward(100)
    t.right(144)
turtle.done()
```

### 利用递归画螺旋图形
![IMAGE](quiver-image-url/CB323C5B4E2ACAA91783219154D7F60F.jpg =171x181)
```
def drawSpiral(t,linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawSpiral(t,linelen-5)
        
drawSpiral(t,100)
turtle.done()
```


### 自相似递归图形 Fractal

自相似递归图形，一个粗糙的几何部分可以分成数个部分，且每一部分都至少近似地是整体缩小后的形状

自然界中分形图形：雪花、闪电、山脉、云朵、海岸线、树
分形：在不同尺度上具有相似的事物

### 递归算法画二叉树
![IMAGE](quiver-image-url/8591788A8A75D012BB74AB598C9B1C6E.jpg =450x198)
符合对递归的调用
```
def tree(branch_len):
    if branch_len > 0:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 30)
        t.left(40)
        tree(branch_len - 30)
        t.right(20)
        t.backward(branch_len)
        
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor = 'green'
t.pensize(2)
tree(120)
turtle.done()
```

#### 分解二叉树递归算法
```
tree(3)
if branch_len > 0:
    t.forward(3)
    t.right(20)
      if branch_len =3 > 0:
        t.forward(2)
        
        t.right(20)
          t.forward(1)
          t.right(20)
          tree(0)
          t.left(40)
          tree(0)
          t.right(20)
          t.backward(1)
  
        t.left(40)
            t.forward(1)
            t.right(20)
            tree(0)
            t.left(40)
            tree(0)
            t.right(20)
            t.backward(1)
        t.right(20)
        t.backward(2)
  
    t.left(40)
      if branch_len =3 > 0:
          t.forward(2)
          
          t.right(20)
          t.forward(1)
          t.right(20)
          tree(0)
          t.left(40)
          tree(0)
          t.right(20)
          t.backward(1)
  
        t.left(40)
            t.forward(1)
            t.right(20)
            tree(0)
            t.left(40)
            tree(0)
            t.right(20)
            t.backward(1)
        t.right(20)
        t.backward(2)
  

      
tree(2)
if branch_len > 0:
  t.forward(2)
  t.right(20)
      t.forward(1)
      t.right(20)
      tree(0)
      t.left(40)
      tree(0)
      t.right(20)
      t.backward(1)
  
  t.left(40)
      t.forward(1)
      t.right(20)
      tree(0)
      t.left(40)
      tree(0)
      t.right(20)
      t.backward(1)
  t.right(20)
  t.backward(2)

tree(1)
if branch_len > 0:
    t.forward(1)
    t.right(20)
    tree(0)   # 不执行
    t.left(40)
    tree(0)   # 不执行
    t.right(20)
    t.backward(1)
```


tree(1)中当画笔长度最后为0时，笔尖向右旋转20°，递归函数变为tree(0)，不会在图上绘画，笔尖再向左旋转40°，tree(0)仍不会在图上绘画，此时笔尖向右旋转20°，笔尖方向长度为1时的节点，此时再沿着这个方向往后退长度为1。


递归条件满足：
- 最终结束条件，当画笔长度<0时不会继续绘画
- 在每次递归调用的时候，减小继续绘画的子树长度，即规模减小
- 画子树时调用自身