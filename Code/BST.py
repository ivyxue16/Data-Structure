class BinarySearchTree:
    def __init__(self):
        self.root = None # Node
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):   # for Node in BST
        return self.root.__iter__()
    

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
        self.payload = val
        self.key = key

    def hasLeftchild(self):
        return self.leftchild

    def hasRightchild(self):
        return self.rightchild

    def isLeftchild(self):
        return self.parent and self.parent.leftchild == self

    def isRightchild(self):
        return self.parent and self.parent.rightchild == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.leftchild or self.rightchild)
    
    def hasAnyChildren(self):
        return self.leftchild or self.rightchild
    
    def hasBothChildren(self):
        return self.leftchild and self.rightchild
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.rightchild = rc
        self.leftchild = lc
        if self.hasLeftchild(self):
            self.leftchild.parent = self
        if self.hasRightchild(self):
            self.rightchild.parent = self



if __name__ == "__main__":
    print(hello(1))
    
