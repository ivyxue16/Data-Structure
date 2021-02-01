
'''
Using recursive list to represent Binary Tree.
'''
def BinaryTree1(r):
    return [r,[],[]]

def insertLeft(root,newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])
    return root

def insertRight(root,newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newbranch,[],t])
    else:
        root.insert(2,[newbranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newval):
    root[0] = newval

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]






class BinaryTree2:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None   # BinaryTree object
        self.rightChild = None   # BinaryTree object

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree2(newNode)
        else:
            t = BinaryTree2(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree2(newNode)
        else:
            t = BinaryTree2(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self,newVal):
        self.key = newVal





if __name__ == "__main__":
    '''
    r = BinaryTree1(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l = getLeftChild(r)
    print(l)

    setRootVal(l,9)
    print(r)
    insertLeft(l,11)
    print(r)
    print(getRightChild(getRightChild(r)))
    '''

    r = BinaryTree2('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getLeftChild().setRootVal('hello')
    r.getRightChild().setRootVal('d')
