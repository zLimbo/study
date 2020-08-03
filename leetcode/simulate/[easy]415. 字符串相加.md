#### [[easy]415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)

> 给定两个字符串形式的非负整数 `num1` 和`num2` ，计算它们的和。
>
> **注意：**
>
> 1. `num1` 和`num2` 的长度都小于 5100.
> 2. `num1` 和`num2` 都只包含数字 `0-9`.
> 3. `num1` 和`num2` 都不包含任何前导零。
> 4. **你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。**



```cpp
// cpp
// simulate

class Solution {
public:
    string addStrings(string num1, string num2) {
        int p1 = num1.size() - 1, p2 = num2.size() - 1;
        int p3 = max(p1, p2);
        string ans(p3+1, '0');
        int sum = 0;
        while (p1 >= 0 && p2 >= 0) {
            sum += (num1[p1] - '0') + (num2[p2] - '0');
            ans[p3] = sum % 10 + '0';
            sum /= 10;
            --p1; --p2; --p3;
        }
        while (p1 >= 0) {
            sum += (num1[p1] - '0');
            ans[p3] = sum % 10 + '0';
            sum /= 10;
            --p1; --p3;
        }
        while (p2 >= 0) {
            sum += (num2[p2] - '0');
            ans[p3] = sum % 10 + '0';
            sum /= 10;
            --p2; --p3;
        }
        if (sum) return "1" + ans;
        return ans;
    }
};
```



```cpp
// cpp
// simulate

class Solution {
public:
    string addStrings(string num1, string num2) {
        int p1 = num1.size() - 1, p2 = num2.size() - 1;
        string ans;
        int sum = 0;
        while (p1 >= 0 || p2 >= 0) {
            if (p1 >= 0) sum += num1[p1--] - '0';
            if (p2 >= 0) sum += num2[p2--] - '0';
            ans.push_back(sum % 10 + '0');
            sum /= 10;
        }
        if (sum) ans.push_back('1');
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```



```python
# python3
# simulate

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        ans = []
        add = 0
        base = ord('0')
        while p1 >= 0 or p2 >= 0:
            add += (ord(num1[p1]) - base) if p1 >= 0 else 0
            add += (ord(num2[p2]) - base) if p2 >= 0 else 0
            ans.append(chr(add % 10 + base))
            add //= 10
            p1 -= 1
            p2 -= 1
        if add: ans.append('1')
        return ''.join(reversed(ans))
```



```python
# python3
# simulate

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        ans = []
        add = 0
        while p1 >= 0 or p2 >= 0:
            add += int(num1[p1]) if p1 >= 0 else 0
            add += int(num2[p2]) if p2 >= 0 else 0
            ans.append(str(add % 10))
            add //= 10
            p1 -= 1
            p2 -= 1
        if add: ans.append('1')
        return ''.join(reversed(ans))
```

