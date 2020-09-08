#### [[hard]51. N 皇后](https://leetcode-cn.com/problems/n-queens/)

> *n* 皇后问题研究的是如何将 *n* 个皇后放置在 *n*×*n* 的棋盘上，并且使皇后彼此之间不能相互攻击。
>
> ![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png)
>
> 上图为 8 皇后问题的一种解法。
>
> 给定一个整数 *n*，返回所有不同的 *n* 皇后问题的解决方案。
>
> 每一种解法包含一个明确的 *n* 皇后问题的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。
>
> ```python
> 示例：
> 
> 输入：4
> 输出：[
>  [".Q..",  // 解法 1
>   "...Q",
>   "Q...",
>   "..Q."],
> 
>  ["..Q.",  // 解法 2
>   "Q...",
>   "...Q",
>   ".Q.."]
> ]
> 解释: 4 皇后问题存在两个不同的解法。
> ```
>
> **提示：**
>
> - 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/n-queens
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// 遍历

class Solution {
public:

    vector<vector<string>> ans;
    int N;

    bool safe(vector<string>& board, int x, int y) {
        for (int i = 0; i < x; ++i) {
            if (board[i][y] == 'Q') return false;
        }
        for (int i = x - 1, j = y - 1; i >= 0 && j >= 0; --i, --j) {
            if (board[i][j] == 'Q') return false;
        }
        for (int i = x - 1, j = y + 1; i >= 0 && j < N; --i, ++j) {
            if (board[i][j] == 'Q') return false;
        }
        return true;
    }


    void dfs(vector<string>& board, int x) {
        if (x == N) {
            ans.push_back(board);
            return;
        }
        for (int j = 0; j < N; ++j) {
            if (safe(board, x, j)) {
                board[x][j] = 'Q';
                dfs(board, x + 1);
                board[x][j] = '.';
            }
        }
    }


    vector<vector<string>> solveNQueens(int n) {
        N = n;
        vector<string> board(n, string(n, '.'));
        dfs(board, 0);
        return ans;
    }
};
```

