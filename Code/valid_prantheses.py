'''
Author: Ivy Xue
Time: 11/29/2020
This file solves Valid Prantheses Problem.

'''



from ADT_Stack import Stack

def praChecker(symbolString):
    """
    Description: Determine whether prantheses appear in pairs and in the right order
    Input Parameter: a string containing a series of brackets
    The function will return whether the string is valid prantheses
    Return: True or False
    """

    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol  == "(":
            s.push(symbol)
        else: 
            if s.isEmpty() == True:
                balanced = False
            else:
                s.pop()
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False


# print(praChecker("(()()()())"))
# print(praChecker(")()("))
# print(praChecker("((((())"))


def praChecker_all(symbolString):
    """
    Description: Determine whether a string of brakets appear in pairs and in the right order
    Input Parameter: a string containing a series of brackets, including (),[],{}
    The function will return whether the string is valid prantheses
    Return: True or False
    """
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced: 
        # use while because of two conditional statements
        # 1. iterate through all indexes
        # 2. the brakets are nested in the correct order
        symbol = symbolString[index]
        if symbol  in "([{":
            s.push(symbol)
        else: 
            if s.isEmpty() == True:
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):   # the exact same type of brakets
                    balanced = False
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    """
    Find out whether the brakets are of the same type.
    """
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)  # the same index shows the same type of brakets




""" print(praChecker_all("{[()]()[]}"))
print(praChecker_all("([)]"))
print(praChecker_all("((([)]])"))
print(praChecker_all("[{()]"))
 """

def isValid(s) -> bool:
    """
    Writing codes within one function
    """
    stack = []
    balanced = True
    index = 0
    brakets = {')':'(',']':'[','}':'{'}
    while index < len(s) and balanced:
        symbol = s[index]
        if symbol in brakets.keys():
            if len(stack) == 0:
                balanced = False
            else:
                if brakets[symbol] != stack[-1]:
                    balanced = False
                else:
                    stack.pop()
        else:   
            stack.append(symbol)            
        index = index + 1
    if len(stack) == 0 and balanced:
        return True
    else:
        return False

""" print(isValid("{[()]()[]}"))
print(isValid("([)]"))
print(isValid("((([)]])"))
print(isValid("[{()]")) """