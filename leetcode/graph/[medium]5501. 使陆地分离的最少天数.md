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
// O((nm)^3)

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



```cpp
// cpp
// 并查集 + Tarjan 找割点算法
// O(nm)

const int dx[4] = {0, 0, 1, -1};
const int dy[4] = {1, -1, 0, 0};

class Solution {
public:

    vector<int> ufs, ufs_size;
    vector<int> dfn, low;
    vector<vector<int>> adj;
    int time;

    // 并查集 
    int ufs_find(int u) {
        return ufs[u] == u ? u : ufs[u] = ufs_find(ufs[u]);
    }

    void ufs_connect(int u, int v) {
        int p = ufs_find(u), q = ufs_find(v);
        if (p == q) return;
        if (ufs_size[p] < ufs_size[q]) {
            ufs[p] = q;
            ufs_size[q] += ufs_size[p];
        } else {
            ufs[q] = p;
            ufs_size[p] += ufs_size[q];
        }
    }

    // tarjan 找割点
    bool tarjan(int u, int p) {
        dfn[u] = low[u] = ++time;
        int child_num = 0;
        for (int v: adj[u]) {
            if (!dfn[v]) {
                ++child_num;
                if ((p == -1 && child_num > 1) 
                    	|| tarjan(v, u) 
                    	|| (p != -1 && low[v] >= dfn[u])) {
                    return true;
                }
                low[u] = min(low[u], low[v]);
            } else if (v != p) {
                low[u] = min(low[u], low[v]);
            }
        }
        return false;
    }

    int minDays(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int N = m * n;
        adj = vector<vector<int>>(N);
        ufs = vector<int>(N, -1);
        ufs_size = vector<int>(N, 1);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (!grid[i][j]) continue;
                int u = i * m + j;
                if (ufs[u] == -1) ufs[u] = u;
                for (int k = 0; k < 4; ++k) {
                    int ni = i + dx[k], nj = j + dy[k];
                    if (ni < 0 || ni >= n || nj < 0 || nj >= m || !grid[ni][nj]) {
                        continue;
                    }
                    int v = ni * m + nj;
                    if (ufs[v] == -1) ufs[v] = v;
                    ufs_connect(u, v);
                    adj[u].push_back(v);
                }
            }
        }
        int set_num = 0;
        for (int i = 0; i < N; ++i) {
            if (ufs[i] != -1 && i == ufs_find(i)) {
                if (++set_num > 1) return 0;
            }
        }
        if (set_num == 0) return 0;
        for (int i = 0; i < N; ++i) {
            if (ufs[i] != -1) {
                dfn = vector<int>(N);
                low = vector<int>(N);
                time = 0;
                return tarjan(i, -1) ? 1 : 2;
            }
        }
        return 0;
    }
};
```

