#### [[medium]96. 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/)

> 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
>
> 示例:
>
> ```bash
> 输入: 3
> 输出: 5
> 解释:
> 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
> 
>    1         3     3      2      1
>     \       /     /      / \      \
>      3     2     1      1   3      2
>     /     /       \                 \
>    2     1         2                 3
> 
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/unique-binary-search-trees
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



math方法：卡塔兰数
$$
C_0 = 1,\quad C_{n+1} = \frac{2(2n + 1)}{n + 2}
$$


```cpp
// cpp
// math

class Solution {
public:
    int numTrees(int n) {
        long long c = 1;
        for (int i = 1; i < n; ++i) {
            c = (c << 1) * (2 * i + 1) / (i + 2);
        }
        return (int)c;
    }
};
```







```python
# python3
# dp

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
```

