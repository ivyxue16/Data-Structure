

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

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/simple-unbalanced.png)

<center> <font color=black>通过左旋让失衡的树恢复平衡</font></center>

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/rotate-right.png)

<center> <font color=black>通过右旋让失衡的树恢复平衡</font></center>

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/balance-factor-derivation.png)

<center> <font color=black>左旋</font></center>

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/hard-unbalanced.png)

<center> <font color=black>更难平衡的树</font></center>

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/bad-rotatation.png)

<center> <font color=black>左旋后，树朝另一个方向失衡</font></center>

![IMAGE](/Users/ivy/Documents/GitHub/Data-Structure/Data-Structure/Graph/rotate-left-right.png)

<center> <font color=black>先右旋，再左旋</font></center>









