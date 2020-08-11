#### [[medium]130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

> 给定一个二维的矩阵，包含 `'X'` 和 `'O'`（**字母 O**）。
>
> 找到所有被 `'X'` 围绕的区域，并将这些区域里所有的 `'O'` 用 `'X'` 填充。
>
> ```shell
> 示例:
> 
> X X X X
> X O O X
> X X O X
> X O X X
> 运行你的函数后，矩阵变为：
> 
> X X X X
> X X X X
> X X X X
> X O X X
> 
> 
> ```
>
> **解释:**
>
> 被围绕的区间不会存在于边界上，换句话说，任何边界上的 `'O'` 都不会被填充为 `'X'`。 任何不在边界上，或不与边界上的 `'O'` 相连的 `'O'` 最终都会被填充为 `'X'`。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/surrounded-regions
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```python
# python3
# dfs

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n, m = len(board), len(board[0])
        
        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m) or board[x][y] != 'O':
                return
            board[x][y] = 'Y'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
```



```cpp
// cpp
// bfs

class Solution {
public:
    static constexpr int dx[4] = {0, 0, 1, -1};
    static constexpr int dy[4] = {1, -1, 0, 0};

    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;
        int n = board.size(), m = board[0].size();

        queue<pair<int, int>> Q;
        for (int i = 0; i < n; ++i) {
            if (board[i][0] == 'O') {
                board[i][0] = 'Y';
                Q.emplace(i, 0);
            }
            if (board[i][m-1] == 'O') {
                board[i][m-1] = 'Y';
                Q.emplace(i, m-1);
            }
        } 
        for (int j = 0; j < m; ++j) {
            if (board[0][j] == 'O') {
                board[0][j] = 'Y';
                Q.emplace(0, j);
            }      
            if (board[n-1][j] == 'O') {
                board[n-1][j] = 'Y';
                Q.emplace(n-1, j);
            }
        }

        while (!Q.empty()) {
            int x = Q.front().first, y = Q.front().second;
            Q.pop();
            for (int k = 0; k < 4; ++k) {
                int xx = x + dx[k], yy = y + dy[k];
                if (0 <= xx && xx < n && 0 <= yy && yy < m && board[xx][yy] == 'O') {
                    board[xx][yy] = 'Y';
                    Q.emplace(xx, yy);
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (board[i][j] == 'Y') board[i][j] = 'O';
                else if (board[i][j] == 'O') board[i][j] = 'X';
            }
        }
    }
};
```

