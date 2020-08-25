#### [[medium]1525. 字符串的好分割数目](https://leetcode-cn.com/problems/number-of-good-ways-to-split-a-string/)

> 给你一个字符串 `s` ，一个分割被称为 「好分割」 当它满足：将 `s` 分割成 2 个字符串 `p` 和 `q` ，它们连接起来等于 `s` 且 `p` 和 `q` 中不同字符的数目相同。
>
> 请你返回 `s` 中好分割的数目。
>
> ```python
> 示例 1：
> 
> 输入：s = "aacaba"
> 输出：2
> 解释：总共有 5 种分割字符串 "aacaba" 的方法，其中 2 种是好分割。
> ("a", "acaba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
> ("aa", "caba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
> ("aac", "aba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
> ("aaca", "ba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
> ("aacab", "a") 左边字符串和右边字符串分别包含 3 个和 1 个不同的字符。
> 示例 2：
> 
> 输入：s = "abcd"
> 输出：1
> 解释：好分割为将字符串分割成 ("ab", "cd") 。
> 示例 3：
> 
> 输入：s = "aaaaa"
> 输出：4
> 解释：所有分割都是好分割。
> 示例 4：
> 
> 输入：s = "acbadbaada"
> 输出：2
> 
> ```
>
> **提示：**
>
> - `s` 只包含小写英文字母。
> - `1 <= s.length <= 10^5`
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/number-of-good-ways-to-split-a-string
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// dp

class Solution {
public:
    int numSplits(string s) {
        int n = s.size();
        vector<int> left(n + 1), right(n + 1);
        bitset<26> lvis, rvis;

        for (int i = 0; i < n; ++i) {
            int lc = s[i] - 'a', rc = s[n - i - 1] - 'a';
            if (!lvis[lc]) {
                lvis.set(lc);
                left[i + 1] = left[i] + 1;
            } else {
                left[i + 1] = left[i];
            }
            if (!rvis[rc]) {
                rvis.set(rc);
                right[i + 1] = right[i] + 1;
            } else {
                right[i + 1] = right[i];
            }
        }

        int ans = 0;
        for (int i = 1; i < n; ++i) {
            if (left[i] == right[n - i]) ++ans;
        }
        return ans;
    }
};
```



```python
# python3
# 前缀和

class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left, right = [0] * (n + 1), [0] * (n + 1)
        ls, rs = set(), set()

        for i in range(n):
            lc, rc = s[i], s[n - i - 1]
            if lc in ls:
                left[i + 1] = left[i]
            else:
                left[i + 1] = left[i] + 1
                ls.add(lc)
            if rc in rs:
                right[i + 1] = right[i]
            else:
                right[i + 1] = right[i] + 1
                rs.add(rc)
        ans = 0
        for i in range(1, n):
            if left[i] == right[n - i]:
                ans += 1
        return ans
```

