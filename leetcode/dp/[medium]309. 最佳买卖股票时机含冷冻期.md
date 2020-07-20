#### [[medium]309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

> 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
>
> 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
>
> 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
> 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
> 示例:
>
> 输入: [1,2,3,0,2]
> 输出: 3 
> 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// dp

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int n = prices.size();
        vector<int> dp(n);

        for (int i = 1; i < n; ++i) {
            dp[i] = dp[i-1];
            for (int j = i-1; j >= 0; --j) {
                int temp = prices[i] - prices[j] + (j >= 2 ? dp[j-2] : 0);
                if (temp > dp[i]) dp[i] = temp;
            }
        }

        return dp[n-1];
    }
};
```



```cpp
// cpp
// dp + 状态转移

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int n = prices.size();
        // dp[i][0]: 手上持有股票的最大收益
        // dp[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        // dp[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        vector<vector<int>> dp(n, vector<int>(3));
        dp[0][0] = -prices[0];
        for (int i = 1; i < n; ++i) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i]);
            dp[i][1] = dp[i-1][0] + prices[i];
            dp[i][2] = max(dp[i-1][1], dp[i-1][2]);
        }

        return max(dp[n-1][1], dp[n-1][2]);
    }
};
```



```python
# python3
# dp + 状态转移

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        p0, p1, p2 = -prices[0], 0, 0
        for i in range(1, n):
            pp0, pp1 = p0, p1
            p0 = max(p0, p2 - prices[i])
            p1 = pp0 + prices[i]
            p2 = max(pp1, p2)
        return max(p1, p2)
```

