#### [[medium]120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

> 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
>
> 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
>
>  
>
> 例如，给定三角形：
>
> [
>      [2],
>     [3,4],
>    [6,5,7],
>   [4,1,8,3]
> ]
> 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
>
>  
>
> 说明：
>
> 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/triangle
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// dp

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> dp(n);

        for (int j = 0; j < n; ++j) {
            dp[j] = triangle[n-1][j];
        }

        for (int i = n-2; i >= 0; --i) {
            for (int j = 0; j <= i; ++j) {
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j];
            }
        }

        return dp[0];
    }
};
```



```python
# python3
# dp

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1][:]
        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
```

