# 置换与逆序数

## 1. **置换的定义**
设有一个由 $n$ 个元素组成的集合 $S = \{1, 2, \dots, n\}$，**置换** $\sigma$ 是一个从集合 $S$ 到自身的双射函数，即：
```math
\sigma: S \to S
```
这个函数将集合中的每个元素 $i$ 重新映射到一个唯一的元素 $\sigma(i)$。换句话说，置换函数对集合中的元素重新排序，而每个元素都被分配到一个新的位置，没有元素重复或遗漏。

例如，对于集合 $S = \{1, 2, 3\}$，一个置换 $\sigma$ 可以是：
```math
\sigma = \begin{pmatrix} 1 & 2 & 3 \\\ 3 & 1 & 2 \end{pmatrix}
```
这表示：
- $1$ 被映射到 $3$；
- $2$ 被映射到 $1$；
- $3$ 被映射到 $2$。

这个置换重新排列了 $S$ 中的元素，将原顺序 $(1, 2, 3)$ 变成了 $(3, 1, 2)$。

### 2. **置换的特殊情况：换位**
你提到的**交换两个值的位置**，就是一种特殊的置换，称为**换位**（Transposition）。换位是只交换两个元素，而其他元素保持不变的置换。

例如，对于集合 $S = \{1, 2, 3, 4\}$，交换 $2$ 和 $4$ 的置换可以表示为：
```math
\tau = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 4 & 3 & 2 \end{pmatrix}
```
这表示：
- $1$ 保持不变；
- $2$ 和 $4$ 交换位置；
- $3$ 保持不变。

换位是一种非常基本的置换，在数学中可以证明**任何置换都可以通过多个换位组合构造出来**。

这意味着，虽然置换可以复杂到重新排列多个元素，但它们可以被分解为一系列的两两交换。

## 3. **置换的两行表示法**
**两行表示法**是一种常用的表示置换的方法，列出置换作用前的元素排列和置换作用后的排列。置换函数 $\sigma$ 映射 $n$ 个元素的排列，可以用如下两行表示：
```math
\sigma = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}
```

第一行表示元素的原始顺序，第二行表示置换后的顺序。

在这个例子中：
- 原序列是 $(1, 2, 3)$；
- 置换后得到的序列是 $(3, 1, 2)$。

这意味着置换 $\sigma$ 将元素 1 置换为 3，将元素 2 置换为 1，将元素 3 置换为 2。

## 4. **两行表示法不是矩阵**
虽然置换的两行表示法看起来像一个 $2 \times n$ 的数组，但它不是矩阵。它只是用来方便表示置换作用的工具，并不是进行矩阵运算的对象。它只展示了置换如何作用于序列中的每个元素：
- 第一行是原来的元素排列；
- 第二行是置换后的元素排列。

两行表示法的主要目的是清楚地展示每个元素在置换前后的位置变化，而不是线性代数中的矩阵。

## 5. **逆序数的定义 (Inversion Number)**
**逆序数**（Inversion Number）是衡量置换中相对于自然顺序有多少对元素的顺序被颠倒的数量。

在一个置换 $\sigma$ 中，如果 $i < j$ 且 $\sigma(i) > \sigma(j)$，那么 $(i, j)$ 是一个**逆序对**。**置换的逆序数就是所有逆序对的数量。**

例如，置换 $\sigma = (2, 1, 3)$：
- $2 > 1$，这是一个逆序对；
- $2 < 3$，不是逆序对；
- $1 < 3$，也不是逆序对。

因此，置换 $\sigma = (2, 1, 3)$ 的逆序数为 1。

## 6. **奇置换与偶置换 (Odd and Even Permutations)**
- **偶置换**：如果置换的逆序数是偶数，则该置换为**偶置换**。偶置换的符号为 $+1$。**偶置换可以表示为偶数次换位的组合**
- **奇置换**：如果置换的逆序数是奇数，则该置换为**奇置换**。奇置换的符号为 $-1$。**奇置换可以表示为奇数次换位的组合**

例如：
- $\sigma = (1, 2, 3)$ 没有逆序对，逆序数为 0，是偶置换。
- $\sigma = (2, 1, 3)$ 有 1 个逆序对，逆序数为 1，是奇置换。

## 6. **置换符号的定义 (Permutation Sign)**
**置换符号**（Permutation Sign，也称为 **符号函数**，**sgn**）定义为：
- 对于偶置换，符号 $\text{sgn}(\sigma) = +1$；
- 对于奇置换，符号 $\text{sgn}(\sigma) = -1$。

置换符号根据置换的逆序数的奇偶性来确定。
- 如果置换的逆序数是偶数，置换符号为 $+1$；
- 如果逆序数是奇数，置换符号为 $-1$。

这在行列式的定义中尤为重要，因为行列式的计算涉及所有置换的符号。

