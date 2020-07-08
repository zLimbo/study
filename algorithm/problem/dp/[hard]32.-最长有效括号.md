#### [[hard]32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

> 给定一个只包含 `'('` 和 `')'` 的字符串，找出最长的包含有效括号的子串的长度。
>
> 示例 1:
>
> 输入: "(()"
> 输出: 2
> 解释: 最长有效括号子串为 "()"
>
> 示例 2:
>
> 输入: ")()())"
> 输出: 4
> 解释: 最长有效括号子串为 "()()"



```cpp
// cpp
// 

class Solution {
public:
    int longestValidParentheses(string s) {
        int ret = 0;
        for (int i = 1; i < s.size(); ++i) {
            if (s[i-1] == '(' && s[i] == ')') {
                pair<int, int> range = expand(s, i-1, i);
                ret = max(ret, range.second - range.first + 1);
                i = range.second;
            }
        }

        return ret;
    }

    pair<int, int> expand(string& s, int left, int right) {
        int lc = 0;
        int rpos = right + 1;
        for ( ; rpos < s.size(); ++rpos) {
            if (s[rpos] == '(') {
                ++lc;
            } else {
                if (lc > 0) {
                    --lc;
                    if (lc == 0) right = rpos;
                } else if (left > 0 && s[left-1] == '(') {
                    --left;
                    right = rpos;
                } else
                    break;
            }
        }
        return make_pair(left, right);
    }
};
```

