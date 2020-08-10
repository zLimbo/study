#### [[medium]1545. 找出第 N 个二进制字符串中的第 K 位](https://leetcode-cn.com/problems/find-kth-bit-in-nth-binary-string/)

> 给你两个正整数 `n` 和 `k`，二进制字符串 `Sn` 的形成规则如下：
>
> - `S1 = "0"`
> - 当 `i > 1` 时，`Si = Si-1 + "1" + reverse(invert(Si-1))`
>
> 其中 `+` 表示串联操作，`reverse(x)` 返回反转 `x` 后得到的字符串，而 `invert(x)` 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）
>
> 例如，符合上述描述的序列的前 4 个字符串依次是：
>
> - `S1 = "0"`
> - `S2 = "0**1**1"`
> - `S3 = "011**1**001"`
> - `S4 = "0111001**1**0110001"`
>
> 请你返回 `Sn` 的 **第 `k` 位字符** ，题目数据保证 `k` 一定在 `Sn` 长度范围以内。
>
> ```shell
> 示例 1：
> 
> 输入：n = 3, k = 1
> 输出："0"
> 解释：S3 为 "0111001"，其第 1 位为 "0" 。
> 示例 2：
> 
> 输入：n = 4, k = 11
> 输出："1"
> 解释：S4 为 "011100110110001"，其第 11 位为 "1" 。
> 示例 3：
> 
> 输入：n = 1, k = 1
> 输出："0"
> 示例 4：
> 
> 输入：n = 2, k = 3
> 输出："1"
> 
> ```
>
> **提示：**
>
> - `1 <= n <= 20`
> - `1 <= k <= 2n - 1`
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/find-kth-bit-in-nth-binary-string
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// recursion

class Solution {
public:   
    char findKthBit(int n, int k) {
        if (n == 1) return '0';
        int mid = 1 << (n-1);
        if (k < mid) return findKthBit(n-1, k);
        if (k > mid) return findKthBit(n-1, (mid << 1) - k) == '0' ? '1' : '0';
        return '1';
    }
};
```



```cpp
// cpp
// Iteration

class Solution {
public:
    char findKthBit(int n, int k) {
        int flag = 1;
        while (n-- > 0) {
            int mid = 1 << n;
            if (k == 1) return flag ? '0' : '1';
            if (k == mid) return flag ? '1' : '0';
            if (k > mid) {
                k = (mid << 1) - k;
                flag = !flag;
            }
        }
        return '0';
    }
};
```



```python
# python3
# recursion

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        mid = 1 << (n - 1)
        if k < mid:
             return self.findKthBit(n - 1, k)
        elif k > mid: 
            return '0' if self.findKthBit(n - 1, (mid << 1) - k) == '1' else '1'
        return '1'
```



```python
# python3
# iteration

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flag = 1
        while n > 0:
            n -= 1
            if k == 1:
                return '0' if flag else '1'
            mid = 1 << n
            if k == mid:
                return '1' if flag else '0'
            if k > mid:
                k = (mid << 1) - k 
                flag = not flag
        return '0'
```

