#### [[medium]343. 整数拆分](https://leetcode-cn.com/problems/integer-break/)

> 给定一个正整数 *n*，将其拆分为**至少**两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
>
> ```shell
> 示例 1:
> 
> 输入: 2
> 输出: 1
> 解释: 2 = 1 + 1, 1 × 1 = 1。
> 示例 2:
> 
> 输入: 10
> 输出: 36
> 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
> 
> 说明: 你可以假设 n 不小于 2 且不大于 58。
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/integer-break
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

官方题解证明：

<img src="[medium]343. 整数拆分/image-20200730092452963.png" alt="image-20200730092452963"  />

<img src="[medium]343. 整数拆分/image-20200730092528760.png" alt="image-20200730092528760"  />

```cpp
//  cpp
// math

class Solution {
public:
    
    inline long long quickPow(long long n, long long m) {
        long long ret = 1;
        while (m) {
            if (m & 1) {
                ret *= n;
            }
            n *= n;
            m >>= 1;
        }
        return ret;
    }

    int integerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;
        int m = n / 3;
        n %= 3;
        if (n == 2e) {
            return quickPow(3, m) * 2;
        } else {
            return quickPow(3, m-1) * (3 + n);
        }
    }
};
```



```python
# python3
# dp

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
```

