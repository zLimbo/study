#### [[medium]416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)

> 给定一个**只包含正整数**的**非空**数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
>
> **注意:**
>
> 1. 每个数组中的元素不会超过 100
> 2. 数组的大小不会超过 200
>
> **示例 1:**
>
> ```
> 输入: [1, 5, 11, 5]
> 
> 输出: true
> 
> 解释: 数组可以分割成 [1, 5, 5] 和 [11].
> ```
>
>  
>
> **示例 2:**
>
> ```
> 输入: [1, 2, 3, 5]
> 
> 输出: false
> 
> 解释: 数组不能分割成两个元素和相等的子集.
> ```



```cpp
// cpp
// dp

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) {
            return false;
        }
        int sum = 0;
        int vMax = -1;
        for (int x: nums) {
            sum += x;
            vMax = max(vMax, x);
        }
        if (sum & 1) {
            return false;
        }
        int target = sum / 2;
        if (vMax > target) {
            return false;
        }
        

        vector<vector<bool>> dp(n, vector<bool>(target + 1));
        for (int i = 0; i < n; ++i) {
            dp[i][0] = true;
        }
        dp[0][nums[0]] = true;
        for (int i = 1; i < n; ++i) {
            int num = nums[i];
            for (int j = 1; j <= target; ++j) {
                if (j >= num) {
                    dp[i][j] = dp[i - 1][j - num] | dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[n - 1][target];
    } 
};
```

