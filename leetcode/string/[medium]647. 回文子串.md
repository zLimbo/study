#### [[medium]647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)

> 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
>
> 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
>
> ```python
> 示例 1：
> 
> 输入："abc"
> 输出：3
> 解释：三个回文子串: "a", "b", "c"
> 示例 2：
> 
> 输入："aaa"
> 输出：6
> 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
> ```
>
> **提示：**
>
> - 输入的字符串长度不会超过 1000 。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/palindromic-substrings
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// Manacher

class Solution {
public:
    int countSubstrings(string s) {
        if (s.empty()) return 0;
        int m = (s.size() << 1) + 1;
        vector<int> f(m);
        int cMax = 0, rMax = 0;
        int ans = 0;

        for (int i = 1; i < m; ++i) {
            int len = 0;
            if (i <= rMax) len = min(rMax - i, f[(cMax << 1) - i]);
            for ( ; 0 <= i - len && i + len < m; ++len) {
                if (((i + len) & 1) && s[(i - len) >> 1] != s[(i + len) >> 1])
                    break;
            }
            f[i] = len - 1;
            if (i + f[i] > rMax) {
                rMax = i + f[i];
                cMax = i;
            }
            ans += (f[i] + 1) >> 1;
        }

        return ans;
    }
};
```

