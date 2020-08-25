#### [[easy]459. 重复的子字符串](https://leetcode-cn.com/problems/repeated-substring-pattern/)

> 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
>
> ```python
> 示例 1:
> 
> 输入: "abab"
> 
> 输出: True
> 
> 解释: 可由子字符串 "ab" 重复两次构成。
> 示例 2:
> 
> 输入: "aba"
> 
> 输出: False
> 示例 3:
> 
> 输入: "abcabcabcabc"
> 
> 输出: True
> 
> 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
> 
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/repeated-substring-pattern
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// 枚举

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for (int i = 2; i <= n; ++i) {
            if (n % i) continue;
            int m = n / i;
            bool ok = true;
            for (int j = m; j < n; ++j) {
                if (s[j] != s[j - m]) {
                    ok = false;
                    break;
                }
            }
            if (ok) return true;
        }
        return false;
    }
};
```



```python
# python3
# 字符串匹配
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
```



```cpp
// cpp
// kmp

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string s2 = s + s;
        return kmp(s2, s, 1) != s.size();
    }

    int kmp(const string& s, const string& t, int start = 0) {
        int sLen = s.size(), tLen = t.size();

        vector<int> next(tLen);
        next[0] = -1;
        int i = 0, j = -1;
        while (i + 1 < tLen) {
            if (j == -1 || t[i] == t[j]) {
                next[++i] = ++j;
                while (next[i] != -1 && s[i] == s[next[i]]) 
                    next[i] = next[next[i]];
            } else {
                j = next[j];
            }
        }
        //for (int x: next) cout << x << " "; cout << endl;

        i = start, j = 0;
        while (i < sLen && j < tLen) {
            if (j == -1 || s[i] == t[j]) {
                // cout << i << " " << j << endl;
                ++i; ++j;
            } else {
                j = next[j];
            }
        }
        // cout << i << " " << j << endl;
        return j == tLen ? i - tLen : -1;
    }
};
```

