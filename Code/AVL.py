class BinarySearchTree:
    def __init__(self):
        self.root = None # Node
        self.size = 0
        self.balanceFactor = 0

    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):   # for Node in BST
        return self.root.__iter__()
    

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftchild():
                self._put(key,val,currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftchild)
        else:
            if currentNode.hasRightchild():
                self._put(key,val,currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightchild)
    def __setitem__(self,k,v):
        self.put(k,v)

    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return 
        if node.parent != None:
            if node.isLeftchild():
                node.parent.balanceFactor += 1
            elif node.isRightchild():
                node.parent.balanceFactor -= 1
            
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)
    
        
    def leftRotate(self,rotRoot):
        newRoot = rotRoot.rightchild
        rotRoot.rightchild = newRoot.leftchild
        if newRoot.leftchild != None:
            newRoot.leftchild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftchild:
                rotRoot.parent.leftchild = newRoot
            else:
                rotRoot.parent.rightchild = newRoot
        newRoot.leftchild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)

    def rightRotate(self,rotRoot):
        newRoot = rotRoot.leftchild
        rotRoot.leftchild = newRoot.rightchild
        if newRoot.rightchild != None:
            newRoot.rightchild.parent = rotRoot
        newRoot.parent = rotRoot.parent 
        if rotRoot.isRoot():
            self.root = newRoot
        else :
            if rotRoot.isLeftchild():
                rotRoot.parent.leftchild = newRoot
            else :
                rotRoot.parent.rightchild = newRoot
        newRoot.rightchild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)
    
    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightchild.balanceFactor > 0:
                self.rightRotate(node.rightchild)
                self.leftRotate(node)
            else: 
                self.leftRotate(node)
        elif node.balanceFactor > 0:
            if node.leftchild.balanceFactor < 0:
                self.leftRotate(node.leftchild)
                self.rightRotate(node)
            else :
                self.rightRotate(node)
                

    def get(self,key):
        res = self._get(key,self.root)
        if res:
            return res.payload
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftchild)
        else:
            return self._get(key,currentNode.rightchild)
    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False


    def delete(self,key):
        if self.size >1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root == key:
            self.size = self.size - 1
            self.root = None
        else:
            raise KeyError("Error, key not in tree")
    def _delitem(self,key):
        self.delete(key)

    def remove(self,currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftchild:
                currentNode.parent.leftchild = None
            else:
                currentNode.parent.rightchild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: 
            if currentNode.hasLeftchild():
                if currentNode.isLeftchild():
                    currentNode.leftchild.parent = currentNode.parent 
                    currentNode.parent.leftchild = currentNode.leftchild
                elif currentNode.isRightchild():
                    currentNode.leftchild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.leftchild
                else: 
                    currentNode.replaceNodeData(currentNode.leftchild.key,currentNode.leftchild.payload,currentNode.leftchild.leftchild,currentNode.leftchild.rightchild)
            else: 
                if currentNode.isLeftchild():
                    currentNode.rightchild.parent = currentNode.parent 
                    currentNode.parent.leftchild = currentNode.rightchild
                elif currentNode.isRightchild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.rightchild
                else: 
                    currentNode.replaceNodeData(currentNode.rightchild.key,currentNode.rightchild.payload,currentNode.rightchild.leftchild,currentNode.rightchild.rightchild)
    

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
        if self.hasLeftchild():
            self.leftchild.parent = self
        if self.hasRightchild():
            self.rightchild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightchild():
            succ = succ.rightchild.findMin()
        else:
            self.parent.rightchild = None
            succ = self.parent.findSuccessor()
            self.parent.rightchild = self
    
    def spliceOut(self):
        if self.isLeaf():
            if self.hasLeftchild():
                self.parent.leftchild = None
            else: 
                self.parent.rightchild = None
        elif self.hasAnyChildren():
            if self.hasLeftchild():
                self.parent.leftchild = self.leftchild
            else: 
                self.parent.rightchild = self.rightchild
            self.leftchild.parent = self.parent
        else: 
            if self.isLeftchild():
                self.parent.leftchild = self.rightchild
            else: 
                self.parent.rightchild = self.rightchild
            self.rightchild.parent = self.parent


    def findMin(self):
        current = self
        while current.hasLeftchild():
            current = current.leftchild
        return current
    
    def __iter__(self): # 中序遍历
        if self:
            if self.hasLeftchild():
                for elem in self.leftchild:
                    yield elem
            yield self.key
            if self.hasRightchild():
                for elem in self.rightchild:
                    yield elem
            



if __name__ == "__main__":
    myTree = BinarySearchTree()
    myTree[3] = 'red'
    myTree[4] = 'blue'
    myTree[6] = 'yellow'
    myTree[2] = 'at'

    print(myTree[3]) # get method