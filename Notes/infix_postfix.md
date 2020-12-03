# 3.5 栈的应用：中缀表达式转换
### 中缀、前缀、后缀表达式概念
**中缀表达式**：操作符(operator)介于操作数(operand)之间。
**中缀表达式优先级**：为了消除歧义，引入操作符”优先级“，同时引入括号表示强制优先级，括号内的优先级更高，在嵌套的括号中，内层的括号优先级更高。

虽然人已经习惯于处理运算优先级，但是计算机运算的时候最好明确规定好运算顺序，这样不需要处理复杂的优先级规则
全括号表达式：在所有表达式项的两边都加上括号
$A+B*C+D$ 可以表示为  $((A+(B*C)+D)$

如果将运算符的位置进行移动，可以得到前缀和后缀表达式：
中缀表达式：$A+B$ 
前缀表达式：$+AB$
后缀表达式：$AB+$
以操作符相对于操作数的位置来定义

使用前缀和后缀表达式的形式可以让括号在表达式中消失，操作符的顺序完全决定运算的顺序，不会有混淆。所以在很多情况下，计算机都避免使用中缀形式。


|中缀表达式|前缀表达式|后缀表达式|
|:-----:|:-----:|:-----:|
|$A + B * C + D$|$ + + A * B C D $|$A B C * + D +$|
|$(A + B) * (C + D)$|$* + A B + C D$|$A B + C D + *$|
|$A * B + C * D$|$ + * A B * C D $|$ A B * C D * + $|
|$A + B + C + D$|$ + + + A B C D$ |$ A B + C + D + $|


### 中缀表达式转换为前缀和后缀形式：
从全括号中缀表达式入手：
$A+B*C$写成全括号形式：$(A + ( B * C))$, 如果把 $*$ 放到)的位置，代替$)$，再删除$($，可以把中缀转换为后缀形式。

**步骤**：
- 将中缀表达式转换为全括号形式
- 将所有的操作符移动到子表达式所在的左括号（前缀）或者右括号（后缀）处，替代括号，再删除所有的括号


### 中缀转换为后缀算法
**流程：**
创建两个数据结构: 空栈(暂存操作符)，空列表(保存需要输出的后缀表达式)

从左到右遍历中缀表达式中的字符列表：
- 如果字符是数字or字母，之间添加到后缀表达式列表末尾
- 如果字符是"(": 压入栈顶
- 如果字符是")": 需要**while**语句 
  - 反复弹出栈顶的操作符，加入到输出结果列表的末尾，直到遇到"("
- 如果字符是"+-*/": 压入栈顶
  - 如果栈不为空，把要进栈的操作符和栈顶操作符比较优先级：用**while**：
    - 如果栈顶的优先级优先级更高，**反复弹出**栈顶的运算符，加入输出列表的末尾(**用while，不可以用if**)
    - 直到栈顶的操作符优先级低于它

```
def infix2Postfix(infixexpr:str) -> str:
    """
    This function will convert Infix Notation to Postfix Notation.
    """

    # A dict indicate oprator's superiority
    prec = {}
    prec['*'] = 3
    prec["/"] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack() # create empty stack
    tokenList = infixexpr.split()  # convert infix str to a list containing operator and operands
    postfixexpr = [] # result list
    
    for token in tokenList:
        # iterate through infix str
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixexpr.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            toptoken = opStack.pop()
            while toptoken != "(": 
                # iterate stack until "(" is found
                # while must be used
                postfixexpr.append(toptoken)
                toptoken = opStack.pop()
        else:
            # pay attention to while, all elements in stack should be compared with the current element
            # if "+" in the stack, and the current str is also "+", the first "+" should be output first
            while opStack.isEmpty() == False and prec[opStack.peek()] >= prec[token]:
                # only 'while' can be used, 'if' is wrong 
                postfixexpr.append(opStack.pop())
            opStack.push(token)

    while opStack.isEmpty() ==  False:
        postfixexpr.append(opStack.pop())

    return ' '.join(postfixexpr)
```


### 后缀表达式求值问题


由于操作符在操作数的后面，需要先暂存操作数，且操作符仅仅作用于离它最近的两个操作数。

流程：
创建空栈用于暂存操作数
从左到右依次扫描列表里的每个字符：
- 如果是操作数，将它转换为整数int，压入栈顶
- 如果是操作符(+-*/)，弹出栈顶的两个操作数，先弹出右操作数，后弹出左操作数（对于-/顺序很重要），进行数学运算，再把计算后的结果压入栈中。
- 继续扫描直到最后栈中只有一个操作数

弹出栈中唯一的数字，返回

```
def evalRPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            num1 = stack.pop() 
            num2 = stack.pop()
            stack.append(str(int(eval(num2 + token + num1))))  # the operands must be evaluated in sequence
        else:
            stack.append(token)
    return int(stack[0])

```


