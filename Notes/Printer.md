# 4.3 队列的应用：打印任务
多人共用一台打印机，采取"先到先服务"的队列策略来执行任务

### 需要弄明白的问题：
- 打印作业系统的容量有多大？
- 在能够接受的等待时间内，系统能容纳多少用户以多高频率提交多少打印任务？

### 模拟算法：
假设条件：
- 在任意一个小时内，大约有10名学生会打印，
- 一小时内，每人会发起2次左右的打印，每次1-20页

打印机的性能：
- 以草稿模式打印：每分钟10页
- 以正常模式打印：每分钟5页，但是质量好

对象：打印任务、打印队列、打印机
- 打印任务的属性：提交时间、打印页数
- 打印队列的属性：FIFO
- 打印机的属性：是否忙、打印速度

如何建模？
过程：生成和提交打印任务
- 确定生成概率：假设任务均匀分布，每小时有20次作业，每180秒产生一次任务，每秒1/180的概率生成一次打印作业
- 确定打印页数：1-20页之间概率相同

实施打印：
- 当前的打印作业：正在打印的作业
- 打印结束倒计时：新作业开始时开始倒计时，时间为0表示打印完毕，可以处理下一个作业

模拟时间：
- 统一的时间框架：以最小单位(秒)均匀流逝的时间，设定结束时间
- 同步所有过程：在一个时间单位内，对**生产打印任**务和**实施打印**两个过程各处理一次


### 模拟流程：
- 创建打印队列对象
- 时间按秒流逝
  - 按照概率生成打印作业，加入打印队列中
  - 如果打印机空闲且打印队列不为空, 取出队首的作业打印，记录该作业的等待时间
  - 如果打印机忙，按照打印速度进行一秒打印
  - 如果当前作业打印完成，打印机进入空闲状态
- 时间用尽，统计平均打印等待时间


- 作业的等待时间：
  - 记录生成作业的时间戳
  - 开始打印时，当前时间减去生成作业的时间戳
- 作业的打印时间：
  - 打印作业的时候，记录作业的页数
  - 开始打印时，用页数除以打印速度
  

### 算法的设计流程
**初始设定**：三个类class：
- 打印机的属性：
  - 输入：打印速度
  - 是否忙
  - 每秒发生什么事，打印倒计时
  - 打印新作业
- 打印任务的属性
  - 作业什么时候生成的
  - 等待时间为多长
  - 有多少页
- 打印队列
  - 空队列

**辅助函数**：两个生成随机数的函数
- 这一秒是否生成任务：生成随机数，假设作业生成服从均匀分布，每秒有$P = \frac{1}{180}$的概率生成一次作业
- 生成作业页数：以相同概率生成1~20中的一个随机整数

**主体程序**：
Input参数：打印机打印速度、观察实验的持续时间
Output参数：平均等待时间

以每秒为单位观察打印机、打印队列、任务生成的过程：
  - 打印机对象
  - 生成新的打印队列：用来依次存放任务
  - 打印任务等待时间列表
  - 循环：对于每一秒
    - 是否生成新任务
      - 是：打印任务生成，加入打印队列
    - 打印机为空&打印队列不为空
      - 计算该任务的等待时间
      - 打印机中加入新任务
    - 打印机在忙：工作倒计时
  - 计算平均等待时间

- 不同参数模拟运行10次

### Code
```
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
```




