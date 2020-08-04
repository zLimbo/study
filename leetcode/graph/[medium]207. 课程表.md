#### [[medium]207. 课程表](https://leetcode-cn.com/problems/course-schedule/)

> 你这个学期必须选修 `numCourse` 门课程，记为 `0` 到 `numCourse-1` 。
>
> 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：`[0,1]`
>
> 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
>
> ```shell
> 示例 1:
> 
> 输入: 2, [[1,0]] 
> 输出: true
> 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
> 示例 2:
> 
> 输入: 2, [[1,0],[0,1]]
> 输出: false
> 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
> ```
>
> **提示：**
>
> 1. 输入的先决条件是由 **边缘列表** 表示的图形，而不是 邻接矩阵 。详情请参见[图的表示法](http://blog.csdn.net/woaidapaopao/article/details/51732947)。
> 2. 你可以假定输入的先决条件中没有重复的边。
> 3. `1 <= numCourses <= 10^5`
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/course-schedule
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// bfs

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> next(numCourses);
        vector<int> prev_cnt(numCourses);

        for (auto &edge: prerequisites) {
            next[edge[1]].push_back(edge[0]);
            ++prev_cnt[edge[0]];
        }

        vector<int> no_prev;
        for (int u = 0; u < numCourses; ++u) 
            if (!prev_cnt[u]) no_prev.push_back(u);
        
        for (int i = 0; i < no_prev.size(); ++i) {
            int u = no_prev[i];
            for (int v: next[u])
                if (!(--prev_cnt[v])) no_prev.push_back(v);
        }

        return no_prev.size() == numCourses;
    }
};
```



```python
# python3
# dfs

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
        vis = [0] * numCourses

        def dfs(u):
            vis[u] = 1
            for v in adj[u]:
                if vis[v] == 1:
                    return False
                if vis[v] == 0:
                    if not dfs(v):
                        return False
            vis[u] = 2
            return True

        for u in range(numCourses):
            if not vis[u] and not dfs(u):
                return False
        return True
```

