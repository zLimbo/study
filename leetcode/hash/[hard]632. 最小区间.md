#### [[hard]632. 最小区间](https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/)

> 你有 `k` 个升序排列的整数数组。找到一个**最小**区间，使得 `k` 个列表中的每个列表至少有一个数包含在其中。
>
> 我们定义如果 `b-a < d-c` 或者在 `b-a == d-c` 时 `a < c`，则区间 [a,b] 比 [c,d] 小。
>
> **示例 1:**
>
> ```shell
> 输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
> 输出: [20,24]
> 解释: 
> 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
> 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
> 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
> ```
>
> **注意:**
>
> 1. 给定的列表可能包含重复元素，所以在这里升序表示 >= 。
> 2. 1 <= `k` <= 3500
> 3. -105 <= `元素的值` <= 105



```cpp
// cpp
// 最小堆 + 多指针


class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        int n = nums.size();
        vector<int> next(n);

        auto cmp = [&](int lhs, int rhs) {
            return nums[lhs][next[lhs]] > nums[rhs][next[rhs]];
        };
        
        priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);
        int left = 0, right = INT_MAX;
        int maxValue = INT_MIN;
        for (int i = 0; i < n; ++i) {
            pq.push(i);
            maxValue = max(maxValue, nums[i][0]);
        }

        while (true) {
            int k = pq.top(); pq.pop();
            int& pos = next[k];
            if (maxValue - nums[k][pos] < right - left) {
                left = nums[k][pos];
                right = maxValue;
            }
            ++pos;
            while (pos < nums[k].size() && nums[k][pos] == nums[k][pos-1]) {
                ++pos;
            }
            if (pos == nums[k].size()) {
                break;
            }
            pq.push(k);
            maxValue = max(maxValue, nums[k][pos]);
        }

        return vector{ left, right };
    }
};
```



```python
# python3
# 最小堆 + 双指针

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        pq = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(pq)
        maxValue = max([vec[0] for vec in nums])
        ansMin, ansMax = -1e5, 1e5

        while True:
            minValue, i, pos = heapq.heappop(pq)
            if maxValue - minValue < ansMax - ansMin:
                ansMin, ansMax = minValue, maxValue
            pos += 1
            while pos < len(nums[i]) and nums[i][pos] == nums[i][pos-1]:
                pos += 1
            if pos == len(nums[i]):
                break
            maxValue = max(maxValue, nums[i][pos])
            heapq.heappush(pq, (nums[i][pos], i, pos))
        return [ansMin, ansMax]
```



```cpp
// cpp
// hash + 滑动数组

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        int n = nums.size();
        map<int, vector<int>> mp;
        for (int i = 0; i < n; ++i) {
            for (int e: nums[i]) {
                mp[e].push_back(i);
            }
        }
        int ansL = -1e5, ansR = 1e5;
        vector<int> cnt(n);
        int k = 0;
        for (auto proIt = mp.begin(), it = mp.begin(); it != mp.end(); ++it) {
            int key = it->first;
            for (int x: it->second) {
                if (++cnt[x] == 1) {
                    ++k;
                }
            }
            while (k == n) {
                int proKey = proIt->first;
                if (key - proKey < ansR - ansL) {
                    ansL = proKey;
                    ansR = key;
                }
                for (int x: proIt->second) {
                    if (--cnt[x] == 0) {
                        --k;
                    }
                }
                ++proIt;
            }
        }
        return vector<int>{ansL, ansR};
    }
};
```



```python
# python3
# hash + 滑动数组

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        indices = collections.defaultdict(list)
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
        sortedKey = sorted(indices.keys())
        ansLeft, ansRight = 1e-5, 1e5
        freq = [0] * n
        cnt = 0
        proKeyId = 0
        for key in sortedKey:
            for x in indices[key]:
                freq[x] += 1
                if freq[x] == 1:
                    cnt += 1
            while cnt == n:
                proKey = sortedKey[proKeyId]
                if key - proKey < ansRight - ansLeft:
                    ansLeft, ansRight = proKey, key
                for x in indices[proKey]:
                    freq[x] -= 1
                    if freq[x] == 0:
                        cnt -= 1
                proKeyId += 1
        return [ansLeft, ansRight]
```

