#### [[hard]546. 移除盒子](https://leetcode-cn.com/problems/remove-boxes/)

> 给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
>
> 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 `k*k` 个积分。
>
> 当你将所有盒子都去掉之后，求你能获得的最大积分和。
>
> ```python
> 示例：
> 
> 输入：boxes = [1,3,2,2,2,3,4,3,1]
> 输出：23
> 解释：
> [1, 3, 2, 2, 2, 3, 4, 3, 1] 
> ----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
> ----> [1, 3, 3, 3, 1] (1*1=1 分) 
> ----> [1, 1] (3*3=9 分) 
> ----> [] (2*2=4 分)
> 
> ```
>
> **提示：**
>
> - `1 <= boxes.length <= 100`
> - `1 <= boxes[i] <= 100`
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/remove-boxes
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// dp

class Solution {
public:
    
    int removeBoxes(vector<int>& boxes) {
        int n = boxes.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(n)));

        return f(dp, boxes, 0, n - 1, 0);
    }

    int f(vector<vector<vector<int>>>& dp, vector<int>& boxes, int x, int y, int z) {
        if (x > y) return 0;
        if (dp[x][y][z]) return dp[x][y][z];
        while (y > x && boxes[y - 1] == boxes[y]) {
            ++z;
            --y;
        }
        dp[x][y][z] = f(dp, boxes, x, y-1, 0) + (z + 1) * (z + 1);
        for (int i = x; i < y; ++i) {
            if (boxes[i] == boxes[y]) {
                dp[x][y][z] = max(dp[x][y][z], f(dp, boxes, x, i, z + 1) + f(dp, boxes, i + 1, y - 1, 0));
            }
        }
        return dp[x][y][z];
    }
};
```





```python
# python3
# dp

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @functools.lru_cache(None)
        def f(x, y, z):
            if x > y:
                return 0
            while y > x and boxes[y - 1] == boxes[y]:
                y -= 1
                z += 1
            ret = f(x, y - 1, 0) + (z + 1) ** 2
            for i in range(x, y):
                if boxes[i] == boxes[y]:
                    ret = max(ret, f(x, i, z + 1) + f(i + 1, y - 1, 0))
            return ret
        
        n = len(boxes)
        return f(0, n - 1, 0)
```



