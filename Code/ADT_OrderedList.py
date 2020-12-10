from ADT_UnorderedList import Node, UnorderedList

class OrderedList(UnorderedList):
    def __init__(self):
        self.head = None
    
    def size(self):
        # O(n)
        current = self.head
        count = 0 
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def isEmpty(self):
        # O(1)
        if self.head == None:
            return True
        else:
            return False

    def search(self,item):
        # O(n)
        current = self.head
        while current is not None:
            if current.getData == item:
                return True
            else:
                if current.getData > item:
                    return False
        current = current.getNext()
        return False
    
    def add(self,item):
        #O(n)
        previous = None
        current = self.head
        stop = False
        while current is not None and not stop:
            if current.value > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current.getNext())
            previous.setNext(temp)

    def remove(self,item):
        # O(n)
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData != item:
                previous = current
                current = current.getNext()
            else:
                found = True
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    



if __name__ == "__main__":
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
