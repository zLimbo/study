#### [[medium]5501. 使陆地分离的最少天数](https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island/)

> 给你一个由若干 `0` 和 `1` 组成的二维网格 `grid` ，其中 `0` 表示水，而 `1` 表示陆地。岛屿由水平方向或竖直方向上相邻的 `1` （陆地）连接形成。
>
> 如果 **恰好只有一座岛屿** ，则认为陆地是 **连通的** ；否则，陆地就是 **分离的** 。
>
> 一天内，可以将任何单个陆地单元（`1`）更改为水单元（`0`）。
>
> 返回使陆地分离的最少天数。
>
> **示例 1：**
>
> ![img]([medium]5501. 使陆地分离的最少天数.assets/1926_island.png)
>
> ```python
> 输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
> 输出：2
> 解释：至少需要 2 天才能得到分离的陆地。
> 将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
> 示例 2：
> 
> 输入：grid = [[1,1]]
> 输出：2
> 解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
> 示例 3：
> 
> 输入：grid = [[1,0,1,0]]
> 输出：0
> 示例 4：
> 
> 输入：grid = [[1,1,0,1,1],
>              [1,1,1,1,1],
>              [1,1,0,1,1],
>              [1,1,0,1,1]]
> 输出：1
> 示例 5：
> 
> 输入：grid = [[1,1,0,1,1],
>              [1,1,1,1,1],
>              [1,1,0,1,1],
>              [1,1,1,1,1]]
> 输出：2
> ```
>
> **提示：**
>
> - `1 <= grid.length, grid[i].length <= 30`
> - `grid[i][j]` 为 `0` 或 `1`
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// dfs

class Solution {
public:
    int n, m;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};

    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& vis, int x, int y) {
        vis[x][y] = true;
        for (int k = 0; k < 4; ++k) {
            int nx = x + dx[k], ny = y + dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < m && grid[nx][ny] && !vis[nx][ny]) {
                dfs(grid, vis, nx, ny);
            }
        }
    }

    int getNum(vector<vector<int>>& grid) {
        int ret = 0;
        vector<vector<bool>> vis(n, vector<bool>(m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] && !vis[i][j]) {
                    ++ret;
                    dfs(grid, vis, i, j);
                }
            }
        }
        return ret;
    }

    int minDays(vector<vector<int>>& grid) {
        n = grid.size(), m = grid[0].size();
        if (getNum(grid) > 1) return 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j]) {
                    grid[i][j] = 0;
                    if (getNum(grid) != 1) return 1;
                    grid[i][j] = 1;
                }
            }
        }
        return 2;
    }
};
```

