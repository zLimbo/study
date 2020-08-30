#### [[hard]214. 最短回文串](https://leetcode-cn.com/problems/shortest-palindrome/)

> 给定一个字符串 ***s***，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
>
> ```python
> 示例 1:
> 
> 输入: "aacecaaa"
> 输出: "aaacecaaa"
> 示例 2:
> 
> 输入: "abcd"
> 输出: "dcbabcd"
> ```



```cpp
// cpp
// kmp

class Solution {
public:
    string shortestPalindrome(string s) {
        if (s.empty()) return "";
        int n = s.size();
        vector<int> fail(n);
        fail[0] = -1;
        int i = 0, j = -1;
        while (i < n - 1) {
            if (j == -1 || s[i] == s[j]) {
                fail[++i] = ++j; 
            } else {
                j = fail[j];
            }
        }
        string ans;
        i = n - 1, j = 0;
        while (i >= 0 && i > j) {
            if (j == -1 || s[i] == s[j]) {
                --i; ++j;
            } else {
                j = fail[j];
            }
        }
        ans.append(s.rbegin(), s.rend() - (i + j + 1));
        ans.append(s);
        return ans;
    }
};
```



```cpp
// cpp
// hash

class Solution {
public:
    string shortestPalindrome(string s) {
        int n = s.size();
        int base = 131, mod = 1000000007;
        int left = 0, right = 0, mul = 1;
        int best = -1;

        for (int i = 0; i < n; ++i) {
            left = ((long long)left * base + s[i]) % mod;
            right = (right + (long long)mul * s[i]) % mod;
            if (left == right) {
                best = i;
            }
            mul = ((long long)mul * base) % mod;
        }
        string prefix(s.rbegin(), s.rend() - (best + 1));
        return prefix + s;
    }
};
```



```cpp
// cpp
// Manacher

class Solution {
public:
    string shortestPalindrome(string s) {
        int n = s.size() * 2 + 1;
        vector<int> f(n);
        int rMax = 0, cMax = 0;
        int best = 0;

        for (int i = 1; i < n; ++i) {
            int len = 0;
            if (i <= rMax) len = min(rMax - i, f[(cMax << 1) - i]);
            for (++len ; 0 <= i - len && i + len < n; ++len) {
                if ((i + len & 1) && s[(i - len) >> 1] != s[(i + len) >> 1]) break;
            }
            f[i] = len - 1;
            if (i + f[i] > rMax) {
                rMax = i + f[i];
                cMax = i;
            }
            if (f[i] == i) best = i;
        }

        string prefix(s.rbegin(), s.rend() - best);
        return prefix + s;
    }
};
```



```python
# python3
# hash

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        base, mod = 131, 1000000007
        left, right, mul = 0, 0, 1
        best = 0

        for i in range(n):
            left = (left * base + ord(s[i])) % mod
            right = (right + mul * ord(s[i])) % mod
            if left == right:
                best = i
            mul = mul * base % mod

        return s[-1:best:-1] + s            
```



```python
# python3
# Manacher

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s) * 2 + 1
        f = [0] * n
        cMax, rMax = 0, 0
        best = 0

        for i in range(1, n):
            k = 1 if (i > rMax) else 1 + min(rMax - i, f[(cMax << 1) - i])
            while 0 <= i - k and i + k < n:
                if i + k & 1 and s[i - k >> 1] != s[i + k >> 1]:
                    break
                k += 1
            f[i] = k - 1
            if i + f[i] > rMax:
                rMax = i + f[i]
                cMax = i
            if i == f[i]:
                best = i
        return s[-1:best-1:-1] + s
```



```python
# python3
# kmp

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        fail = [-1] * n
        i, j = 0, -1
        while i < n - 1:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                fail[i] = j
            else:
                j = fail[j]
        i, j = n - 1, j
        while j < i:
            if j == -1 or s[i] == s[j]:
                i -= 1
                j += 1
            else:
                j = fail[j]
        
        return s[-1:i+j:-1] + s
```

