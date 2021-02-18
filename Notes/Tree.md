# 9.1 树

#### 树的属性
- 层次性：按层次构建，越笼统越靠近顶部，越具体越靠近底部
- 一个节点的所有子节点与另一个节点的所有子节点无关
- 叶子节点独一无二

### 术语

#### 节点
节点是树的基础部分。它可以有自己的名字，我们称作“键”。节点也可以带有附加信息，我们称作“有效载荷”。有效载荷信息对于很多树算法来说不是重点，但它常常在使用树的应用中很重要。

#### 边
边是树的另一个基础部分。两个节点通过一条边相连，表示它们之间存在关系。除了根节点以外，其他每个节点都仅有一条入边，出边则可能有多条。

#### 根节点
根节点是树中唯一没有入边的节点。

#### 路径
路径是由边连接的有序节点列表。比如，哺乳纲一食肉目→猫科→猫属一家猫就是一条路径。

#### 子节点
一个节点通过出边与子节点相连。
#### 父节点
一个节点是其所有子节点的父节点。
#### 兄弟节点
具有同一父节点的节点互称为兄弟节点。

#### 子树
一个父节点及其所有后代的节点和边构成一棵子树。

#### 叶子节点
叶子节点没有子节点。比如，图6—1中的人和黑猩猩都是叶子节点。

####  层数
节点n的层数是从根节点到n的唯一路径长度。由定义可知，根节点的层数是0

#### 高度

树的高度是其中节点层数的最大值。

### 树的定义
1. 定义一：树由节点及连接节点的边构成。树有以下属性：
- 有一个根节点；
- 除根节点外，其他每个节点都与其唯一的父节点相连；
- 从根节点到其他每个节点都有且仅有一条路径；
- 二叉树：每个节点最多有两个子节点。

2. 定义二：一棵树要么为空，要么由一个根节点和零棵或多棵子树构成，子树本身也是一棵树。每棵子树的根节点通过一条边连到父树的根节点。从树的递归定义可知，图中的树至少有4个节点，因为三角形代表的子树必定有一个根节点。这棵树或许有更多的节点，但必须更深入地查看子树后才能确定。

### 树的实现
#### 1. 列表之列表
**Code**
```
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
```

2. 定义BinaryTree 类
实现的方法：
- 初始化：key, 左子树，右子树
- 插入左子树 insertLeft(self,newNode)
- 插入右子树 insertRight(self,newNode)
- 查找左子树 getLeftChild(self)
- 查找右子树 getRightChild(self)
- 查找根 getRootVal(self)

**解析树**：全括号表达式转换为树，计算值
注：最外面不能漏写括号，否则无法得到正确答案，形成树的时候值会被后面的数字覆盖。

**算法**：
构建解析树的第一步是将表达式字符串拆分成标记列表。需要考虑4种标记：左括号、右括号、运算符和操作数。我们知道，左括号代表新表达式的起点，所以应该创建一棵对应该表达式的新树。反之，遇到右括号则意味着到达该表达式的终点。我们也知道，操作数既是叶子节点，也是其运算符的子节点。此外，每个运算符都有左右子节点。

有了上述信息，便可以定义以下4条规则：

（1）如果当前标记是'('，就为当前节点添加一个左子节点，并下沉至该子节点；
（2）如果当前标记在列表['+'， '—'， '/'，'*']中，就将当前节点的值设为当前标记对应的运算符；为当前节点添加一个右子节点，并下沉至该子节点；
（3）如果当前标记是数字，就将当前节点的值设为这个数并返回至父节点；
（4）如果当前标记是')'，就跳到当前节点的父节点。

标记父节点需要通过栈来记录，每当要下沉至当前节点的子节点时，先将当前节点压到栈中，当要返回当前节点的父节点时，就将父节点从栈中弹出来。

注：
- 下沉：currentTree = currentTree.getLeftChild()



**Code**
```
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
```

**解析树 Code**
```
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
```



### 树的遍历：根节点的位置
- 前序遍历：根左右
- 中序遍历：左根右
- 后序遍历：左右根

**树的遍历Code**
```
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
```



