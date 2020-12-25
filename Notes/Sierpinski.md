# 5.5 递归：谢尔宾斯基三角形
5.5 递归：谢尔宾斯基三角形
谢尔宾斯基三角形

从三角形的每条边的中点分割出新的三角形，
真正地谢尔宾斯基完全不可见，三角形的面积为0，周长无穷，介于一维和二维之间的分数维（约为1.585维）构造。

![IMAGE](quiver-image-url/F17CB7FD9D308B3A88A1018C064F2618.jpg =404x131)

我们无法做出degree -> ∞，只能做出degree有限的图形。

### 算法拆解

根据自相似的性质，谢尔宾斯基三角形是由三个尺寸减半的谢尔宾斯基三角形按照品字型拼叠而成。

在degree有限的情况下，degree = n的三角形是由3个degree = n- 1的三角形拼叠的，同时这三个degree = n-1的三角形的边长为degree = n的三角形的边长的一半（规模减小）。
当degree=0时，谢尔宾斯基三角形为等边三角形，递归基本结束条件。

### 符合递归算法
- 基本结束条件：degree = 0
- 向着规模减小的方向进行：degree - 1，边长减半
- 调用自身

从大到小画完小的三角形再画其他分支的大三角形

![IMAGE](quiver-image-url/D0C52203F925C8C9ED2AE9B5287DC2C0.jpg =467x335)



### Code

from turtle import *

def drawTriangle(points:List,color:List,myTurtle) -> None:
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMid(p1:tuple,p2:tuple)->tuple: 
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(points:List,degree:int,myTurtle):
    colormap = ['blue','red','green','white','yellow','violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree-1,myTurtle)
        sierpinski([points[1],getMid(points[1],points[0]),getMid(points[1],points[2])],degree-1,myTurtle)
        sierpinski([points[2],getMid(points[2],points[0]),getMid(points[2],points[1])],degree-1,myTurtle)

myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [(-300,-150),(0,300),(300,-150)]  
sierpinski(myPoints,2,myTurtle)
myWin.exitonclick()


### 分解递归

def sierpinski(points,degree=2,myTurtle):
  drawTriangle(points,colormap[degree],myTurtle)
  if degree =2> 0:
      sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],1,myTurtle)
        drawTriangle([p0,A,B],colormap[1],myTurtle)
        sierpinski([p0,A,B],1,myTurtle)
          drawTriangle([p0,A,B],colormap[1],myTurtle)
          if degree = 1 >0:
            sierpinski([p0,d,e],1,myTurtle)
              drawTriangle([p0,d,e],colormap[1],myTurtle)
            sierpinski([A,d,f],1,myTurtle)
              drawTriangle([A,d,f],colormap[1],myTurtle)
            sierpinski([B,e,f],1,myTurtle)
              drawTriangle([B,e,f],colormap[1],myTurtle)
    

      sierpinski([points[1],getMid(points[1],points[0]),getMid(points[1],points[2])],1,myTurtle)
        sierpinski([p1,A,C],1,myTurtle)
      
      sierpinski([points[2],getMid(points[2],points[0]),getMid(points[2],points[1])],1,myTurtle)
        sierpinski([p2,B,C],1,myTurtle)


  
degree = 1
sierpinski([p0,A,B],1,myTurtle)
  drawTriangle([p0,A,B],colormap[1],myTurtle)
  if degree = 1 >0:
    sierpinski([p0,d,e],1,myTurtle)
      drawTriangle([p0,d,e],colormap[1],myTurtle)
    
    sierpinski([A,d,f],1,myTurtle)
      drawTriangle([A,d,f],colormap[1],myTurtle)
    
    sierpinski([B,e,f],1,myTurtle)
      drawTriangle([B,e,f],colormap[1],myTurtle)
    


degree = 0
def sierpinski(points,0,myTurtle):
  drawTriangle(points,colormap[degree],myTurtle)
  if degree > 0:
      sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree-1,myTurtle)
      sierpinski([points[1],getMid(points[1],points[0]),getMid(points[1],points[2])],degree-1,myTurtle)
      sierpinski([points[2],getMid(points[2],points[0]),getMid(points[2],points[1])],degree-1,myTurtle)

degree = 0
sierpinski([p0,d,e],1,myTurtle):
  drawTriangle([p0,d,e],colormap[1],myTurtle)
```