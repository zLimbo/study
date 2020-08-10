#### [[easy]696. 计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings/)

> 给定一个字符串 `s`，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
>
> 重复出现的子串要计算它们出现的次数。
>
> ```shell
> 示例 1 :
> 
> 输入: "00110011"
> 输出: 6
> 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
> 
> 请注意，一些重复出现的子串要计算它们出现的次数。
> 
> 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
> 示例 2 :
> 
> 输入: "10101"
> 输出: 4
> 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
> 
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/count-binary-substrings
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
> ```
>
> **注意：**
>
> - `s.length` 在1到50,000之间。
> - `s` 只包含“0”或“1”字符。



```python
# python3
#

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, lastCnt, cnt, prev = 0, 0, 0, s[0]
        for c in s:
            if c == prev:
                cnt += 1
            else:
                ans += min(lastCnt, cnt)
                lastCnt, cnt, prev = cnt, 1, c
        ans += min(lastCnt, cnt)
        return ans
```



```cpp
// cpp
//

class Solution {
public:
    int countBinarySubstrings(string s) {
        int ans = 0;
        char prev = s[0];
        int last_cnt = 0, cnt = 0;

        for (char c: s) {
            if (c == prev) ++cnt;
            else {
                ans += last_cnt < cnt ? last_cnt : cnt;
                last_cnt = cnt;
                cnt = 1;
                prev = c;
            }
        }
        ans += last_cnt < cnt ? last_cnt : cnt;
        return ans;
    }
};
```

