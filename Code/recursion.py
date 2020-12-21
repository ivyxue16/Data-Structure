"""
Recursion examples
This file is the illustration of recursion.
"""

from typing import List

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

def drawSpiral(t,linelen):
    
    # Example to show recursion
    
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawSpiral(t,linelen-5)


# drawSpiral(t,100)
# turtle.done()
'''

def reverselist(numlist:List) ->List:
    '''
    reverse a list using recursion
    '''
    if len(numlist) == 1:
        return [numlist[-1]]
    else:
        return [numlist[-1]] + reverselist(numlist[:-1])

print(reverselist([1,2,3,4,5,6]))