class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0
    def __repr__(self):
        return "Binary Heap Class"

    def insert(self,key):
        self.heaplist.append(key)
        self.currentsize = self.currentsize + 1
        self.percUp(self.currentsize)
    
    def percUp(self,i):
        while i // 2 > 0 :
            if self.heaplist[i] < self.heaplist[i // 2]:
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i // 2] 
                self.heaplist[i // 2] = temp
            i // 2



    def delMin(self):
        retVal = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.heaplist.pop()
        self.currentsize = self.currentsize - 1
        self.percDown(1)
        return retVal
    def percDown(self,i):
        while i * 2 <= self.currentsize:
            mc = self.minChild(i)
            if self.heaplist[mc] < self.heaplist[i]:
                self.heaplist[mc],self.heaplist[i] = self.heaplist[i],self.heaplist[mc]
            i = mc
    def minChild(self,i):
        if i * 2 > self.currentsize:
            return self.currentsize
        else:
            if self.heaplist[ i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1



