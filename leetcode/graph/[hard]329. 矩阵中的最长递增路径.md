#### [[hard]329. 矩阵中的最长递增路径](https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/)

> 给定一个整数矩阵，找出最长递增路径的长度。
>
> 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
>
> **示例 1:**
>
> ```shell
> 输入: nums = 
> [
>   [9,9,4],
>   [6,6,8],
>   [2,1,1]
> ] 
> 输出: 4 
> 解释: 最长递增路径为 [1, 2, 6, 9]。
> ```
>
> **示例 2:**
>
> ```shell
> 输入: nums = 
> [
>   [3,4,5],
>   [3,2,6],
>   [2,2,1]
> ] 
> 输出: 4 
> 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
> ```



```cpp
// cpp
// dfs + 记忆

class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty()) return 0;
        int n = matrix.size(), m = matrix[0].size();
        vector<vector<int>> dp(n, vector<int>(m));
        int ret = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                ret = max(ret, dfs(matrix, dp, i,  j));
            }
        }
        return ret;
    }

    int dfs(vector<vector<int>>& mat, vector<vector<int>>& dp, int i, int j) {
        int n = mat.size(), m = mat[0].size();
        if (dp[i][j]) return dp[i][j];
        dp[i][j] = 1;

        int max_path = 0;
        if (i > 0 && mat[i][j] < mat[i-1][j]) {
            max_path = max(max_path, dfs(mat, dp, i-1, j));
        }
        if (i < n-1 && mat[i][j] < mat[i+1][j]) {
            max_path = max(max_path, dfs(mat, dp, i+1, j)); 
        }
        if (j > 0 && mat[i][j] < mat[i][j-1]) {
            max_path = max(max_path, dfs(mat, dp, i, j-1));
        }
        if (j < m-1 && mat[i][j] < mat[i][j+1]) {
            max_path = max(max_path, dfs(mat, dp, i, j+1));
        }
        dp[i][j] += max_path;
        return dp[i][j];
    }
};
```



```cpp
// cpp
// dfs + 记忆

class Solution {
public:
    static constexpr int dirs[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int n, m;

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty()) return 0;
        n = matrix.size();
        m = matrix[0].size();
        vector<vector<int>> dp(n, vector<int>(m));
        int ret = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                ret = max(ret, dfs(matrix, dp, i,  j));
            }
        }
        return ret;
    }

    int dfs(vector<vector<int>>& mat, vector<vector<int>>& dp, int i, int j) {
        if (dp[i][j]) return dp[i][j];

        int max_path = 0;
        for (int k = 0; k < 4; ++k) {
            int x = i + dirs[k][0], y = j + dirs[k][1];
            if (x >= 0 && x < n && y >= 0 && y < m && mat[i][j] < mat[x][y]) {
                max_path = max(max_path, dfs(mat, dp, x, y));
            }
        }
        dp[i][j] = max_path + 1;
        return dp[i][j];
    }
};
```



```python
# python3
# dfs + 记忆

class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 0
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn))
            return best + 1

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for row in range(rows):
            for column in range(columns):
               ans = max(ans, dfs(row, column))
        return ans 
```

