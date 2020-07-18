#### [[hard]97. 交错字符串](https://leetcode-cn.com/problems/interleaving-string/)

> 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
>
> ```shell
> 示例 1:
> 
> 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
> 输出: true
> 示例 2:
> 
> 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
> 输出: false
> ```
>
> 
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/interleaving-string
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// dp

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size(), m = s2.size(), t = s3.size();
        if (n + m != t) return false;

        vector<vector<int>> dp(n+1, vector<int>(m+1));

        dp[0][0] = true;
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= m; ++j) {
                int k = i + j - 1;
                if (i > 0) {
                    dp[i][j] |= (dp[i-1][j] & (s1[i-1] == s3[k]));
                }
                if (j > 0) {
                    dp[i][j] |= (dp[i][j-1] & (s2[j-1] == s3[k]));
                }
            }
        }

        return dp[n][m];
    }
};
```



```python
# python3
# dp

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        if n + m != t:
            return False
        dp = [[False] * (m+1) for _ in range(n+1)]

        dp[0][0] = True
        for i in range(n+1):
            for j in range(m+1):
                k = i + j - 1
                if i > 0:
                    dp[i][j] |= (dp[i-1][j] & (s1[i-1] == s3[k]))
                if j > 0:
                    dp[i][j] |= (dp[i][j-1] & (s2[j-1] == s3[k]))
        return dp[n][m]
```



```python
# python3
# stack + dfs

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        if n + m != t:
            return False
        vis = [[False] * (m+1) for _ in range(n+1)]
        s = [(0, 0)]
        while s:
            i, j = s.pop()
            if i + j == t:
                return True
            if vis[i][j]:
                continue
            vis[i][j] = True
            k = i + j
            if i < n and s1[i] == s3[k]:
                s.append((i+1, j))
            if j < m and s2[j] == s3[k]:
                s.append((i, j+1))
        return False 
        
```

