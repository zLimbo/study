#### [[medium]64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

> 给定一个包含非负整数的 *m* x *n* 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
>
> **说明：**每次只能向下或者向右移动一步。
>
> **示例:**
>
> ```shell
> 输入:
> [
>   [1,3,1],
>   [1,5,1],
>   [4,2,1]
> ]
> 输出: 7
> 解释: 因为路径 1→3→1→1→1 的总和最小。
> ```



```cpp
// cpp
// dp + 滚动数组

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        int n = grid.size(), m = grid[0].size();
        vector<int> dp(m, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            dp[0] = dp[0] + grid[i][0];
            for (int j = 1; j < m; ++j) {
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j];
            }
        }
        return dp[m-1];
    }
};
```



```python
# python3
# dp + 滚动数组

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        dp = [math.inf for _ in range(m)]
        dp[0] = 0
        for i in range(n):
            dp[0] += grid[i][0]
            for j in range(1, m):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[m-1]
```



```java
// java
// dp + 滚动数组

class Solution {
    public int minPathSum(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        int[] dp = new int[m];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 0; i < n; ++i) {
            dp[0] += grid[i][0];
            for (int j = 1; j < m; ++j) {
                dp[j] = (dp[j-1] < dp[j] ? dp[j-1] : dp[j]) + grid[i][j];
            }
        }
        
        return dp[m-1];
    }
}
```

