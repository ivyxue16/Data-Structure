'''
Author: Ivy Xue
Time: 12/4/2020
This file solves Hot Potato Problem.
Description: 
The children’s game Hot Potato. 
In this game, children line up in a circle and pass an item from neighbor to neighbor as fast as they can. 
At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. 
Play continues until only one child is left.
Input Parameter: 
names: a list containing all the children names.
num: after num chilren, the next children will go out of the circle

The function will return postfix notation
Return: str
'''

from ADT_Queue import Queue
from typing import List

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


if __name__ == "__main__":
    print(hot_potato(('Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'), 5))
