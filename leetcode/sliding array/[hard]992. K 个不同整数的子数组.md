#### [[hard]992. K 个不同整数的子数组](https://leetcode-cn.com/problems/subarrays-with-k-different-integers/)

> 给定一个正整数数组 `A`，如果 `A` 的某个子数组中不同整数的个数恰好为 `K`，则称 `A` 的这个连续、不一定独立的子数组为*好子数组*。
>
> （例如，`[1,2,3,1,2]` 中有 `3` 个不同的整数：`1`，`2`，以及 `3`。）
>
> 返回 `A` 中*好子数组*的数目。
>
>  
>
> **示例 1：**
>
> ```
> 输入：A = [1,2,1,2,3], K = 2
> 输出：7
> 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
> ```
>
> **示例 2：**
>
> ```
> 输入：A = [1,2,1,3,4], K = 3
> 输出：3
> 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
> ```
>
>  
>
> **提示：**
>
> 1. `1 <= A.length <= 20000`
> 2. `1 <= A[i] <= A.length`
> 3. `1 <= K <= A.length`



```cpp
// cpp
// 恰好 -> 最多, 双指针,滑动数组

class Solution {
public:
    int subarraysWithKDistinct(vector<int>& A, int K) {
        return atMostKDistinct(A, K) - atMostKDistinct(A, K - 1);
    }

    int atMostKDistinct(vector<int>& A, int K) {
        int n = A.size();
        unordered_map<int, int> um;
        int res = 0;
        int cnt = 0;
        int left = 0, right = 0;

        while (right < n) {
            if (um[A[right]] == 0) {
                ++cnt;
            }
            ++um[A[right]];
            ++right;

            while (cnt > K) {
                if (--um[A[left]] == 0) {
                    --cnt;
                }
                ++left;
            }

            res += right - left;
        }

        return res;
    }
};
```

