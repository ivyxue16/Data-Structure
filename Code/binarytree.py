from ADT_Stack import Stack
import operator


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






class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None   # BinaryTree object
        self.rightChild = None   # BinaryTree object

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
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


def buildParseTree(expstr:str):
    explist = expstr.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in explist:
        if i == "(":
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    opers = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()


def preorder(tree:BinaryTree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
def postorder(tree:BinaryTree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree:BinaryTree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())



if __name__ == "__main__":
    '''
    r = BinaryTree1(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l = getLeftChild(r)
    # print(l)

    setRootVal(l,9)
    # print(r)
    insertLeft(l,11)
    # print(r)
    # print(getRightChild(getRightChild(r)))
    

    
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
    
    '''
    # fpexp = ' ( ( 7 + 3 ) * ( 5 - 2 ) ) '
    fpexp = '( 3 +  ( 5 * 7 ) )'
    eTree = buildParseTree(fpexp)
    # print(eTree.getRootVal())
    # print(eTree.leftChild.getRootVal())

    # op = operator.add
    # print(op(1,2))
    print(evaluate(eTree))

    # x = ( ( 7 + 3 ) * ( 5 - 2 ) )
    # print(x)

