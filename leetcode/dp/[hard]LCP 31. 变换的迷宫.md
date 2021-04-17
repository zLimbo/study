#### [[hard]LCP 31. 变换的迷宫](https://leetcode-cn.com/problems/Db3wC1/)

> 某解密游戏中，有一个 N*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 `(n-1,m-1)` 位置。迷宫变化规律记录于 `maze` 中，`maze[i]` 表示 `i` 时刻迷宫的地形状态，`"."` 表示可通行空地，`"#"` 表示陷阱。
>
> 地形图初始状态记作 `maze[0]`，此时小力位于起点 `(0,0)`。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。
>
> 小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：
>
> - 临时消除术：将指定位置在下一个时刻变为空地；
> - 永久消除术：将指定位置永久变为空地。
>
> 请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？
>
> **注意： 输入数据保证起点和终点在所有时刻均为空地。**
>
> **示例 1：**
>
> > 输入：`maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]`
> >
> > 输出：`true`
> >
> > 解释：
> > ![maze.gif](https://pic.leetcode-cn.com/1615892239-SCIjyf-maze.gif)
>
> **示例 2：**
>
> > 输入：`maze = [[".#.","..."],["...","..."]]`
> >
> > 输出：`false`
> >
> > 解释：由于时间不够，小力无法到达终点逃出迷宫。
>
> **示例 3：**
>
> > 输入：`maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]`
> >
> > 输出：`false`
> >
> > 解释：由于道路不通，小力无法到达终点逃出迷宫。
>
> **提示：**
>
> - `1 <= maze.length <= 100`
> - `1 <= maze[i].length, maze[i][j].length <= 50`
> - `maze[i][j]` 仅包含 `"."`、`"#"`



```cpp
// cpp
// dp

const int dx[] = {0, 0, 1, -1, 0};
const int dy[] = {1, -1, 0, 0, 0};

class Solution {
public:
    bool escapeMaze(vector<vector<string>>& maze) {
        int T = maze.size(), m = maze[0].size(), n = maze[0][0].size();
        int dp[T][m][n][5];
        int can[m][n][2];
        memset(dp, 0, sizeof(dp));
        memset(can, 0, sizeof(can));

        for (int t = 0; t < T; ++t) {
            for (int k = 0; k < 4; ++k) {
                dp[t][m - 1][n - 1][k] = 1;
            }
        }

        can[m - 1][n - 1][0] = can[m - 1][n - 1][1] = 1;

        for (int t = T - 2; t >= 0; --t) {
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    for (int k = 0; k < 4; ++k) {
                        int u = k & 1, v = k & 2;
                        for (int d = 0; d < 5; ++d) {
                            int ni = i + dx[d], nj = j + dy[d];
                            if (0 <= ni && ni < m && 0 <= nj && nj < n) {
                                if (maze[t + 1][ni][nj] == '.') {
                                    dp[t][i][j][k] |= dp[t + 1][ni][nj][k];
                                } else {
                                    if (!u) {
                                        dp[t][i][j][k] |= dp[t + 1][ni][nj][k | 1];
                                    }
                                    if (!v) {
                                        dp[t][i][j][k] |= can[ni][nj][u];
                                    }
                                }
                            }
                        }
                    }
                    can[i][j][0] |= dp[t][i][j][2];
                    can[i][j][1] |= dp[t][i][j][3];
                }
            }
        }

        return dp[0][0][0][0];
    }
};
```



```java
// java
// dp

class Solution {
    public boolean escapeMaze(List<List<String>> maze) {
        int T = maze.size(), n = maze.get(0).size(), m = maze.get(0).get(0).length();

        boolean[][][][] dp = new boolean[T][n][m][5];
        boolean[][][] can = new boolean[n][m][2];

        for (int t = 0; t < T; ++t) {
            for (int k = 0; k < 4; ++k) {
                dp[t][n - 1][m - 1][k] = true;
            }
        }

        can[n - 1][m - 1][0] = can[n - 1][m - 1][1] = true;

        int[] dx = {1, -1, 0, 0, 0};
        int[] dy = {0, 0, 1, -1, 0};

        for (int t = T - 2; t >= 0; --t) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    for (int k = 0; k < 4; ++k) {
                        int u = k & 1, v = k & 2;
                        for (int d = 0; d < 5; ++d) {
                            int ni = i + dx[d], nj = j + dy[d];
                            if (0 <= ni && ni < n && 0 <= nj && nj < m) {
                                if (maze.get(t + 1).get(ni).charAt(nj) == '.') {
                                    dp[t][i][j][k] |= dp[t + 1][ni][nj][k];
                                } else {
                                    if (0 == u) {
                                        dp[t][i][j][k] |= dp[t + 1][ni][nj][k | 1];
                                    }
                                    if (0 == v) {
                                        dp[t][i][j][k] |= can[ni][nj][u];
                                    }
                                }
                            }
                        }
                    }
                    can[i][j][0] |= dp[t][i][j][2];
                    can[i][j][1] |= dp[t][i][j][3];
                }
            }
        }

        return dp[0][0][0][0];
    }
}
```

