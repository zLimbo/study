#### [[easy]392. 判断子序列](https://leetcode-cn.com/problems/is-subsequence/)

> 给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。
>
> 你可以认为 **s** 和 **t** 中仅包含英文小写字母。字符串 **t** 可能会很长（长度 ~= 500,000），而 **s** 是个短字符串（长度 <=100）。
>
> 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。
>
> **示例 1:**
> **s** = `"abc"`, **t** = `"ahbgdc"`
>
> 返回 `true`.
>
> **示例 2:**
> **s** = `"axc"`, **t** = `"ahbgdc"`
>
> 返回 `false`.
>
> **后续挑战** **:**
>
> 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？



```python
# python3
# 双指针法

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = len(s)
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == n:
                    return True
        return False
```



后续挑战解法：

```cpp
// cpp
// dp

class Solution {
public:
    vector<bool> isSubsequence(vector<string>& vs, string t) {
        int m = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(26));

        for (int i = 0; i < 26; ++i) {
            dp[m][i] = m;
        }

        for (int i = m - 1; i >= 0; --i) {
            for (int j = 0; j < 26; ++j) {
                if (t[i] == ('a' + j)) {
                    dp[i][j] = i;
                } else {
                    dp[i][j] = dp[i + 1][j];
                }
            }
        }
        
        vector<bool> ans(vs.size());
        for (int i = 0; i < vs.size(); ++i) {
            string& s = vs[i];
            int p = 0;
            bool isMatch = true;
            for (int j = 0; j < s.size(); ++j) {
                if (dp[p][s[i] - 'a'] == m) {
                    isMatch = false;
                    break;
                }
                p = dp[p][s[i] - 'a'] + 1;
            }
            ans[i] = isMatch;
        }

        return ans;
    }
};
```

