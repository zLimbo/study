#### [[medium]5477. 排布二进制网格的最少交换次数](https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid/)

> 给你一个 `n x n` 的二进制网格 `grid`，每一次操作中，你可以选择网格的 **相邻两行** 进行交换。
>
> 一个符合要求的网格需要满足主对角线以上的格子全部都是 **0** 。
>
> 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 **-1** 。
>
> 主对角线指的是从 `(1, 1)` 到 `(n, n)` 的这些格子。
>
> **示例 1：**
>
> ![img]([medium]5477. 排布二进制网格的最少交换次数/fw.jpg)
>
> ```shell
> 输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
> 输出：3
> ```
>
> **示例 2：**
>
> ![img]([medium]5477. 排布二进制网格的最少交换次数/e3.jpg)
>
> ```shell
> 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
> 输出：0
> ```
>
> **示例 3：**
>
> ![img]([medium]5477. 排布二进制网格的最少交换次数/e3.jpg)
>
> ```
> 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
> 输出：0
> ```
>
> **提示：**
>
> - `n == grid.length`
> - `n == grid[i].length`
> - `1 <= n <= 200`
> - `grid[i][j]` 要么是 `0` 要么是 `1` 。



```cpp
// cpp
// 插入排序

class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> zero(n);

        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            for (int j = n-1; j >= 0; --j) {
                if (grid[i][j] == 0) {
                    ++cnt;
                } else {
                    break;
                }
            }
            zero[i] = cnt;
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int zeroNum = n - i - 1;
            int j = i;
            for ( ; j < n; ++j) {
                if (zero[j] >= zeroNum) {
                    break;
                }
            }
            if (j == n) {
                return -1;
            }
            for ( ; j > i; --j) {
                zero[j] = zero[j-1];
                ++ans;
            }
        }
        return ans;
    }
};
```

