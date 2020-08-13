#### [[medium]43. 字符串相乘](https://leetcode-cn.com/problems/multiply-strings/)

> 给定两个以字符串形式表示的非负整数 `num1` 和 `num2`，返回 `num1` 和 `num2` 的乘积，它们的乘积也表示为字符串形式。
>
> ```python
> 示例 1:
> 
> 输入: num1 = "2", num2 = "3"
> 输出: "6"
>     
> 示例 2:
> 
> 输入: num1 = "123", num2 = "456"
> 输出: "56088"
> ```
>
> **说明：**
>
> 1. `num1` 和 `num2` 的长度小于110。
> 2. `num1` 和 `num2` 只包含数字 `0-9`。
> 3. `num1` 和 `num2` 均不以零开头，除非是数字 0 本身。
> 4. **不能使用任何标准库的大数类型（比如 BigInteger）**或**直接将输入转换为整数来处理**。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/multiply-strings
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// simulate 

class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";
        int n = num1.size(), m = num2.size();
        string prod(n + m, '0');
        // 乘法运算
        for (int i = n - 1; i >= 0; --i) {
            int x = num1[i] - '0';
            int add = 0;    // 进位
            for (int j = m - 1; j >= 0; --j) {
                add += x * (num2[j] - '0') + (prod[i + j + 1] - '0') ;
                prod[i + j + 1] = add % 10 + '0';
                add /= 10;
            }
            prod[i] = add + '0';
        }
        // 删除前导零
        if (prod[0] == '0') { 
            int cnt = 1;
            while (prod[cnt] == '0') ++cnt;
            prod.erase(0, cnt);
        }
        return prod;
    }
};
```



```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n, m = len(num1), len(num2)
        prod = ['0'] * (n + m)
        for i in range(n - 1, -1, -1):
            x = ord(num1[i]) - ord('0')
            add = 0
            for j in range(m - 1, -1, -1):
                add += x * (ord(num2[j]) - ord('0')) + (ord(prod[i + j + 1]) - ord('0'))
                prod[i + j + 1] = chr(add % 10 + ord('0'))
                add //= 10
            prod[i] = chr(add + ord('0'))
        start = 0
        while prod[start] == '0':
            start += 1
        return ''.join(prod[start:])
```

