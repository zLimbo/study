#### [[medium]718. 最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)

> 给两个整数数组 `A` 和 `B` ，返回两个数组中公共的、长度最长的子数组的长度。



```cpp
// cpp

class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        int ret = 0;
        
        for (int i = m-1; i >= 0; --i) {
            for (int j = n-1; j >= 0; --j) {
                if (A[i] == B[j]) dp[i][j] = dp[i+1][j+1] + 1;
                ret = max(ret, dp[i][j]);
            }
        }
        return ret;
    }
};
```

Python3

```python
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (A[i] == B[j]):
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(row) for row in dp)

        
```

Java

```java
class CQueue {
    public Stack<Integer> stackPush;
    public Stack<Integer> stackPop;

    public CQueue() {
        stackPush = new Stack<Integer>();
        stackPop = new Stack<Integer>();
    }
    
    public void appendTail(int value) {
        stackPush.push(value);
    }
    
    public int deleteHead() {
        if (stackPop.isEmpty())
            while (!stackPush.isEmpty())
                stackPop.push(stackPush.pop());
        return stackPop.isEmpty() ? -1 : stackPop.pop();
    }
}
```

