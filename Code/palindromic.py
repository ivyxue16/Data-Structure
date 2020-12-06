'''
Author: Ivy Xue
Time: 12/6/2020
This file will determine whether a character is a palindromic word.
Input Parameter: str
The function will return True/False
Return: bool
'''

class Deque():
    def __init__(self):
        self.items = []
    def addFront(self,item):
        return self.items.append(item)
    def addRear(self,item):
        return self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)


def palChecker(aString:str) -> bool:
    d = Deque()
    # generate a new deque to store the string
    for ch in aString:
        d.addRear(ch)
    
    stillEqual = True

    while d.size() > 1 and stillEqual:
        """
        when there are more than 1 character in string, loop 
        """
        # the first character and the last character of palindromic are the same
        front = d.removeFront()
        last = d.removeRear()
        if front != last:  
            stillEqual =  False 
            break
    return stillEqual


if __name__ == "__main__":
    print(palChecker("lsdhf"))
    print(palChecker('radar'))
    print(palChecker('toot'))


