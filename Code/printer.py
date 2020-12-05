'''
Author: Ivy Xue
Time: 12/5/2020
This file simulates how printer works.
Generate Printing queue, Printer Object, Task needed to be printed 
Input Parameter: ppm(printing speed), duration(1hr)
The function will return average time waiting for printing.
Return: 
'''

import random 
from typing import List

class Queue:
    """
    Generate priting queue
    """
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)



class Printer:
    """
    """
    def __init__(self,ppm:int):
        self.ppm = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def busy(self):
        if self.currentTask == None :
            return False
        else:
            return True

    def startNext(self,newTask:classmethod):
        self.currentTask = newTask
        self.timeRemaining = (newTask.getPages() / self.ppm) * 60
    
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None


class Task():
    def __init__(self,time:int):
        self.timeStamp = time
        self.pages = random.randrange(1,21)
    def getPages(self):
        return self.pages 
    def getStamp(self):
        return self.timeStamp
    def waitingTime(self,currenTime):
        return currenTime - self.timeStamp


def newPrinterTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSceconds, ppm):

    printingQueue = Queue()
    waitingTimes = []
    labPrinter = Printer(ppm)

    for currentSecond in range(numSceconds):

        if newPrinterTask() == True:
            task = Task(currentSecond)
            printingQueue.enqueue(task)

        if labPrinter.busy() != True and printingQueue.isEmpty() == False:
            nextTask = printingQueue.dequeue()
            waitingTimes.append(task.waitingTime(currentSecond))
            labPrinter.startNext(nextTask)

        labPrinter.tick()
        
    averageWaitTime = sum(waitingTimes) / len(waitingTimes)
    
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWaitTime, printingQueue.size()))

for i in range(10):
    simulation(3600,5)


        