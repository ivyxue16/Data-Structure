
def BinaryTree(r):
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


if __name__ == "__main__":
    r = BinaryTree(3)
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

