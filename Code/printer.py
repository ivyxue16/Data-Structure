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
    This class object contain settings of printer.

    """
    def __init__(self,ppm:int):
        self.ppm = ppm  # printing speed per minute
        self.currentTask = None  # Task is a class object
        self.timeRemaining = 0  # the current task still need  n seconds to complete printing

    def busy(self):
        '''
        indicate whether the printer is busy or not
        '''
        if self.currentTask == None :
            return False
        else:
            return True

    def startNext(self,newTask:classmethod):
        '''
        This method enables printer to start new task
        '''
        self.currentTask = newTask # class obeject
        self.timeRemaining = (newTask.getPages() / self.ppm) * 60 # how many seconds needed to complete printing
    
    def tick(self):
        '''
        simulate printer working process
        '''
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1 
            if self.timeRemaining <= 0:
                self.currentTask = None


class Task():
    '''
    Generate attributes related to new task
    '''
    def __init__(self,time:int):
        self.timeStamp = time
        self.pages = random.randrange(1,21) # 1-20 pages each time
    def getPages(self):
        return self.pages 
    def getStamp(self):
        return self.timeStamp 
    def waitingTime(self,currenTime):
        return currenTime - self.timeStamp # how long this task will be waiting


def newPrinterTask():
    """
    Whether or not to generate a new task for this second
    """
    num = random.randrange(1,181) # Probability = 1/180 to generate a task per second
    if num == 180: # any number between 1-180 could be accepted
        return True
    else:
        return False


def simulation(numSceconds, ppm):
    '''
    Input parameters:
    numSeconds: duration of time period, eg. 1 hr
    ppm: printing speed, argument of Printer class
    '''

    printingQueue = Queue() # generate a new printing Queue
    waitingTimes = [] # all waiting times
    labPrinter = Printer(ppm) # generate a new Printer

    for currentSecond in range(numSceconds):
        # this loop will simulate every second in one hour

        if newPrinterTask() == True:
            # if new task is generate this second
            task = Task(currentSecond)  # a new task class would be generated
            printingQueue.enqueue(task)  # the new task will enter the printing queue

        if labPrinter.busy() != True and printingQueue.isEmpty() == False:
            # when the printer is not busy and there is task in the printing queue
            # the top task will be got out of the queue and enter the printer
            # find out waiting time for this task since it has been generated 
            nextTask = printingQueue.dequeue()
            waitingTimes.append(task.waitingTime(currentSecond))
            labPrinter.startNext(nextTask) # Printer start new task

        labPrinter.tick() # if the printer is busy, the printer will work until the current task is completed
        
    averageWaitTime = sum(waitingTimes) / len(waitingTimes) 
    
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWaitTime, printingQueue.size()))


# use different printing speed to simulate the process
for i in range(10):
    simulation(3600,5)

for i in range(10):
    simulation(3600,10)

        