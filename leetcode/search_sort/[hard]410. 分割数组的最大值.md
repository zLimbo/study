#### [[hard]410. 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/)

> 给定一个非负整数数组和一个整数 *m*，你需要将这个数组分成 *m* 个非空的连续子数组。设计一个算法使得这 *m* 个子数组各自和的最大值最小。
>
> **注意:**
> 数组长度 *n* 满足以下条件:
>
> - 1 ≤ *n* ≤ 1000
> - 1 ≤ *m* ≤ min(50, *n*)
>
> **示例:**
>
> ```shell
> 输入:
> nums = [7,2,5,10,8]
> m = 2
> 
> 输出:
> 18
> 
> 解释:
> 一共有四种方法将nums分割为2个子数组。
> 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
> 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/split-array-largest-sum
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处



```python
# python3
# 值二分查找

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        # 最小值必然落在[max(nums), sum(nums)] 之间
        left, right = max(nums), sum(nums) 
        while left < right:
            medium = (left + right) // 2
            # 计算子数组和 sub_sum 不大于 medium （以趋近left）的数目
            # 若 count > m，说明 medium 过小，目标值应落在 [medium + 1, right]
            # 若 count < m，说明 medium 过大，目标值应落在 [left, medium - 1]
            # 若 count == m, 可能还存在更小的 medium，
            # 因为计数是子数组不大于medium，故目标值应落在 [left, medium] 
            sub_sum = 0
            count = 0
            for i in range(n):
                sub_sum += nums[i]
                if sub_sum > medium:
                    count += 1
                    sub_sum = nums[i]
            count += 1	# 剩一个未统计
            if count <= m:
                right = medium # 合并两种情况
            else:
                left = medium + 1
        return left
        
```

```cpp
// cpp
// dp

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int n = nums.size();
        vector<vector<long long>> dp(n+1, vector<long long>(m+1, LLONG_MAX));
        vector<long long> sub(n+1);

        for (int i = 0; i < n; ++i) {
            sub[i+1] = sub[i] + nums[i];
        }
        dp[0][0] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= min(i, m); ++j) {
                for (int k = j-1; k < i; ++k) {
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i] - sub[k]));
                }
            }
        }

        return dp[n][m];
    }
};
```

```cpp
// cpp
// 值二分查找

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long long low = 0, high = 0;

        for (int v: nums) {
            high += v;
            if (low < v) low = v;
        }

        while (low < high) {
            long long mid = low + ((high - low) >> 1);
            int count = 0;
            long long sub = 0;
            for (int v: nums) {
                sub += v;
                if (sub > mid) {
                    ++count;
                    sub = v;
                }
            }
            ++count;
            if (count <= m) high = mid;
            else low = mid + 1;
        }

        return (int)low;
    }
};
```

```java
// java
// 值二分查找

class Solution {
    public int splitArray(int[] nums, int m) {
        long low = 0, high = 0;

        for (int v: nums) {
            high += v;
            if (low < v) low = v;
        }

        while (low < high) {
            long mid = low + ((high - low) >> 1);
            long sub = 0;
            long count = 0;
            for (int v: nums) {
                sub += v;
                if (sub > mid) {
                    ++count;
                    sub = v;
                }
            }
            ++count;
            if (count <= m) high = mid;
            else low = mid + 1;
        }

        return (int)low;
    }
}
```



```cpp
// cpp
// dp

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int n = nums.size();
        vector<vector<long long>> dp(n, vector<long long>(m));

        dp[0][0] = nums[0];
        for (int i = 1; i < n; ++i) dp[i][0] = dp[i-1][0] + nums[i];

        for (int i = 1; i < n; ++i) {
            int rb = min(m-1, i);
            for (int j = 1; j <= rb; ++j) {
                long long t = nums[i];
                long long tmp = LLONG_MAX;
                for (int k = i-1; k >= j-1; --k) {
                    tmp = min(tmp, max(t, dp[k][j-1]));
                    t += nums[k];
                }
                dp[i][j] = tmp;
            }
        }
        return dp[n-1][m-1];
    }
};
```

