'''
Author: Ivy Xue
Time: 12/3/2020
This file converts infix notation to postfix notation.
Input Parameter: str
The function will return postfix notation
Return: str
'''


from typing import List

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def infix2Postfix(infixexpr:str) -> str:
    """
    This function will convert Infix Notation to Postfix Notation.
    """

    # A dict indicate oprator's superiority
    prec = {}
    prec['*'] = 3
    prec["/"] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack() # create empty stack
    tokenList = infixexpr.split()  # convert infix str to a list containing operator and operands
    postfixexpr = [] # result list
    
    for token in tokenList:
        # iterate through infix str
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixexpr.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            toptoken = opStack.pop()
            while toptoken != "(": 
                # iterate stack until "(" is found
                # while must be used
                postfixexpr.append(toptoken)
                toptoken = opStack.pop()
        else:
            # pay attention to while, all elements in stack should be compared with the current element
            # if "+" in the stack, and the current str is also "+", the first "+" should be output first
            while opStack.isEmpty() == False and prec[opStack.peek()] >= prec[token]:
                # only 'while' can be used, 'if' is wrong 
                postfixexpr.append(opStack.pop())
            opStack.push(token)

    while opStack.isEmpty() ==  False:
        postfixexpr.append(opStack.pop())

    return ' '.join(postfixexpr)


def evalRPN(tokens: List[str]) -> int:
    """
    Calculate the value of postfix expression
    """

    stack = []

    for token in tokens:
        if token in "+-*/":
            num1 = stack.pop() 
            num2 = stack.pop()
            stack.append(str(int(eval(num2 + token + num1))))  # the operands must be evaluated in sequence
        else:
            stack.append(token)
    return int(stack[0])






if __name__ == "__main__":
    # print(infix2Postfix(" A + B  * C + D "))
    print(evalRPN(["2", "1", "+", "3", "*"]))
    print(evalRPN(["4", "13", "5", "/", "+"]))
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

