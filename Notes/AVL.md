

### AVL树的定义和平衡因子

AVL树能自动维持平衡， 以发明者G.M.Adelson-Velskii和E.M.Landis的名字命名。

AVL与普通二叉搜索树都能实现映射抽象数据类型的方式，唯一的区别是性能。AVL树需要记录每个节点的平衡因子，即左右子树的高度差。

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/unbalanced.png)

<center> <font color=black>带平衡因子的右倾树</font></center>


$$
Balance Factor = height(leftSubTree) - height(rightSubTree)
$$

- 平衡因子> 0：左倾
- 平衡因子< 0：右倾
- 平衡因子= 0：完全平衡

平衡树：平衡因子为-1、0，1

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/worst-case-AVL.png)





<center> <font color=black>左倾AVL树的最坏情况</font></center>





当高度为$h$时，节点数 $$ N_h $$ 是：
$$
N_h = 1 + N_{h-1}+N_{h-2}
$$


与斐波那契数列很类似，可以由此推导出AVL数的节点数计算高度的公式。
在斐波那契数列中，第$$i$$个数是：
$$
F_0 = 0
$$

$$F_1 = 1$$
$$F_i = F_{i-1} + F_{i-2}, i ≥ 2$$
随着斐波那契数列的增长，$\frac{F_i}{F_{i-1}}$越来越接近黄金分割比例$\phi=\frac{1+\sqrt{5}}{2}$，将$F_i$近似为$F_i=\frac{\phi^i}{\sqrt{5}}$，将$N_h$的等式重写为：
$$N_h = F_{h+2}-1,h≥ 1$$
用黄金分割近似替换，得到：
$$N_h = \frac{\phi^{h+2}}{\sqrt{5}} - 1$$
移项，两边以2位底取对数，求h，得到：
$$ logN_h+1 = (H+2)log\phi-\frac{1}{2}log5 $$
$$ h=\frac{logN_h+1-2log\phi+\frac{1}{2}log5}{log\phi}$$
$$ h = 1.44logN_h$$
在任何时间，AVL树的高度都等于节点数取对数再乘以一个常数(1.44)，对于搜索AVL来说是好事，因为时间复杂度被限制为$O(logN)$

### 往树中插人一个键

所有新键都是以叶子节点插入的，因为新叶子节点的平衡因子是零，所以新插节点没有什么限制条件。但插入新节点后，必须更新父节点的平衡因子。新的叶子节点对其父节点平衡因子的影响取决于它是左子节点还是右子节点。

- 如果是右子节点，父节点的平衡因子减一。

- 如果是左子节点，则父节点的平衡因子加一。

  

这个关系可以递归地应用到每个祖先，直到根节点。既然更新平衡因子是递归过程，就来检查以下两种基本情况：

- 递归调用抵达根节点；

- 父节点的平衡因子调整为零；可以确信，如果子树的平衡因子为零，那么祖先节点的平衡因子将不会有变化。

### 树的再平衡

为了让AVL树恢复平衡，需要在树上进行一次或多次旋转：

#### 左旋

- 将右子节点(节点B)提升为子树的根节点。  

- 将旧根节点(节点A)作为新根节点的左子节点。  

- 如果新根节点(节点B)已经有一个左子节点，将其作为新左子节点(节点A)的右子节  点。注意，因为节点B之前是节点A的右子节点，所以此时节点A必然没有右子节点。  因此，可以为它添加新的右子节点，而无须过多考虑。  





![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/simple-unbalanced.png)

<center> <font color=black>通过左旋让失衡的树恢复平衡</font></center>

#### 右旋

- 将左子节点(节点C)提升为子树的根节点。  

- 将旧根节点(节点E)作为新根节点的右子节点。  

- 如果新根节点(节点C)已经有一个右子节点(节点D)，将其作为新右子节点(节点E)  的左子节点。注意，因为节点C之前是节点E的左子节点，所以此时节点E必然没有左子节点。因此，可以为它添加新的左子节点，而无须过多考虑。  



![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/rotate-right.png)

<center> <font color=black>通过右旋让失衡的树恢复平衡</font></center>

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/balance-factor-derivation.png)

<center> <font color=black>左旋</font></center>

#### 更新平衡因子

根节点为$$x$$的子树，高度记为$$h_x$$，由定义可知：
$$
newBal(B) = h_A - h_c
$$

$$
oldBal(B) = h_A - h_D
$$



旧$$h_D$$也可以写为$$1+max(h_C,h_E)$$，即两棵子树中高度的较大值+1，因为$$h_C$$与$$h_E$$不变，代入第二个等式，得到
$$
oldBal(B) = h_A-(1+max(h_C,h_E))
$$

$$
newBal(B) - oldBal(B) =  h_A - h_C - (h_A - h_D)
$$

$$
newBal(B) - oldBal(B) =  h_A - h_C - (h_A - (1+max(h_C,h_E)))
$$

$$
newBal(B) - oldBal(B) =  1+max(h_C,h_E)- h_C
$$



将$$oldBal(B)$$移到等式右边，利用$$max(a,b)-c=max(a-c,b-c)$$可得：
$$
newBal(B)  = oldBal(B) + 1+max(h_C- h_C,h_E- h_C)
$$
$$h_E- h_C = -h_D$$ 

最终可得：
$$
newBal(B)  = oldBal(B) + 1+max(0,-oldBal(D))
$$

$$
newBal(B)  = oldBal(B) + 1 - min(0,oldBal(D))
$$

对应的代码为

```python
rotRoot.BalanceFactor = rotRoot.BalanceFactor + 1 - min(0,newRoot.BalanceFactor)
newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)
```





#### 双旋

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/hard-unbalanced.png)

<center> <font color=black>更难平衡的树</font></center>

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/bad-rotatation.png)

<center> <font color=black>左旋后，树朝另一个方向失衡</font></center>



 围绕节点C做一次右旋，  再围绕节点A做一次左旋，就能让子树恢复平衡。  



![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/rotate-left-right.png)

<center> <font color=black>先右旋，再左旋</font></center>

  

要解决这种问题，必须遵循以下规则。  

- 如果子树需要左旋，首先检查右子树的平衡因子。如果右子树左倾，就对右子树做一次右旋，再围绕原节点做一次左旋。  
- 如果子树需要右旋，首先检查左子树的平衡因子。如果左子树右倾，就对左子树做一次左旋，再围绕原节点做一次右旋。  





















