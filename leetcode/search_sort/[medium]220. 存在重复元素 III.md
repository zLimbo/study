#### [[medium]220. 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii/)

> 给你一个整数数组 `nums` 和两个整数 `k` 和 `t` 。请你判断是否存在 **两个不同下标** `i` 和 `j`，使得 `abs(nums[i] - nums[j]) <= t` ，同时又满足 `abs(i - j) <= k` 。
>
> 如果存在则返回 `true`，不存在返回 `false`。
>
>  
>
> **示例 1：**
>
> ```
> 输入：nums = [1,2,3,1], k = 3, t = 0
> 输出：true
> ```
>
> **示例 2：**
>
> ```
> 输入：nums = [1,0,1,1], k = 1, t = 2
> 输出：true
> ```
>
> **示例 3：**
>
> ```
> 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
> 输出：false
> ```
>
>  
>
> **提示：**
>
> - `0 <= nums.length <= 2 * 104`
> - `-231 <= nums[i] <= 231 - 1`
> - `0 <= k <= 104`
> - `0 <= t <= 231 - 1`



```cpp
// cpp
// 桶 0(n)

class Solution {
public:

    int getId(int x, long w) {
        return x < 0 ? (x + 1LL) / w - 1 : x / w;
    }

    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        unordered_map<int, int> bucket;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            long x = nums[i];
            int id = getId(x,  t + 1LL);
            if (bucket.count(id)) return true;
            if (bucket.count(id - 1) && abs(x - bucket[id - 1]) <= t) return true;
            if (bucket.count(id + 1) && abs(bucket[id + 1] - x) <= t) return true;
            bucket[id] = x;
            if (i >= k) bucket.erase(getId(nums[i - k],  t + 1LL));
        }
        return false;
    }
};

```



```cpp
// cpp
// sort: O(long(min(n, k)))

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        set<int> st;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            if (st.count(x)) return true;
            auto it = st.lower_bound(max(x, INT_MIN + t) - t);
            if (it != st.end() && *it <= min(x, INT_MAX - t) + t) return true;
            st.insert(x);
            if (i >= k) st.erase(nums[i - k]);
        }
        return false;
    }
};
```

