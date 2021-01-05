"""
Recursion examples
This file is the illustration of recursion.
"""

from typing import List
import turtle

'''
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())
'''

def listsum(numlist:List) -> int:
    '''
    This function will add up all the numbers in the lists using recursion.
    '''
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

# print(listsum([1,3,5,7,9]))


def baseConvert(num:int,base:int) -> str:
    '''
    This function will convert Decimal system to any base(2-16)
    num: decimal sytem number
    base: convert to base system

    eg. 67(10) convert to base 7 is 124(7)
    eg. 12(10) convert to base 2 is 1100(2)
    '''
    convertString = '0123456789ABCDEF'
    if num // base == 0:
        return convertString[num]
    else:
        return  baseConvert(num // base,base) + convertString[num % base]
    
# print(baseConvert(67,7)) 124
# print(baseConvert(12,2)) 1100
# print(baseConvert(1453,16)) 5AD


'''
import turtle
t = turtle.Turtle()

t.pencolor('red')
t.pensize(3)
for i in range(5):
    t.forward(100)
    t.right(144)
turtle.done()
'''

def drawSpiral(t,linelen):
    
    # Example to show recursion
    
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawSpiral(t,linelen-5)


# drawSpiral(t,100)
# turtle.done()


def reverselist(numlist:List) ->List:
    '''
    reverse a list using recursion
    '''
    if len(numlist) == 1:
        return [numlist[-1]]
    else:
        return [numlist[-1]] + reverselist(numlist[:-1])

# print(reverselist([1,2,3,4,5,6]))

def drawspiral2(t,linelen):

    if linelen > 0: # use if not while
        t.backward(linelen)
        t.left(90)
        drawspiral2(t,linelen - 5)

# drawspiral2(t,100)
# turtle.done()
'''

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
'''


def fab(n):
    '''
    Time complexity is O(2^n)
    Space complexity is O(n)
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)

# print(fab(2)) 1
# print(fab(5)) 5
# print(fab(20)) 6765


'''
Recursion example: Sierpinski Triangle
'''
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
        # iteration all points at the same degree
        sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree-1,myTurtle)
        sierpinski([points[1],getMid(points[1],points[0]),getMid(points[1],points[2])],degree-1,myTurtle)
        sierpinski([points[2],getMid(points[2],points[0]),getMid(points[2],points[1])],degree-1,myTurtle)

'''
myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [(-300,-150),(0,300),(300,-150)]  # list of 3 tuples
sierpinski(myPoints,5,myTurtle)
myWin.exitonclick()
'''


def moveTower(height,fromPole,withPole,toPole):
    '''
    This function solves the Tower of Hanoi problem
    '''
    if height >= 1:
        moveTower(height-1,fromPole,toPole,withPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height-1,withPole,fromPole,toPole)

def moveDisk(disk,fromPole,toPole):
    '''This function print out the path of a disk'''
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")

# moveTower(3,"#1","#2","#3")


### find min number of coins 
def rec(change,coins):
    minCoins = change
    if change in coins:
        return 1
    else:
        for i in [c for c in coins if c <= change]:
            sumCoins = 1 + rec(change-i,coins)
            if sumCoins < minCoins:
                minCoins = sumCoins
    return minCoins

# print(rec(43,[1,2,5,10,25]))


### find min number of coins 
### use knownresult to store values
def recDC(change:int,coins:List,knownresult:List) -> int:
    minCoins = change
    if change in coins:
        return 1
    elif knownresult[change] > 0:
        return knownresult[change]
    else:
        for i in [c for c in coins if c <= change]:
            sumCoins = 1 + recDC(change-i,coins,knownresult)
            if sumCoins < minCoins:
                minCoins = sumCoins
                knownresult[change] = minCoins
    return minCoins

# x = 101
# print(recDC(x,[1,5,10,21,25],[0]*(x+1)))