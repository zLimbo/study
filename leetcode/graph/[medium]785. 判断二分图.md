#### [[medium]785. 判断二分图](https://leetcode-cn.com/problems/is-graph-bipartite/)

> 给定一个无向图graph，当这个图为二分图时返回true。
>
> 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
>
> graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。
>
> ```shell
> 示例 1:
> 输入: [[1,3], [0,2], [1,3], [0,2]]
> 输出: true
> 解释: 
> 无向图如下:
> 0----1
> |    |
> |    |
> 3----2
> 我们可以将节点分成两组: {0, 2} 和 {1, 3}。
> 
> 示例 2:
> 输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
> 输出: false
> 解释: 
> 无向图如下:
> 0----1
> | \  |
> |  \ |
> 3----2
> 我们不能将节点分割成两个独立的子集。
> ```
>
> 注意:
>
> graph 的长度范围为 [1, 100]。
> graph[i] 中的元素的范围为 [0, graph.length - 1]。
> graph[i] 不会包含 i 或者有重复的值。
> 图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/is-graph-bipartite
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// bfs

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int sz = graph.size();
        vector<int> belong(sz, -1);
    
        for (int i = 0; i < sz; ++i) {
            if (belong[i] == -1) {
                queue<int> q;
                q.push(i);
                belong[i] = 0;
                while (!q.empty()) {
                    int cur = q.front(); q.pop();
                    int newBelong = !belong[cur];
                    for (int n: graph[cur]) {
                        if (belong[n] == -1) {
                            belong[n] = newBelong;
                            q.push(n);
                        }
                        else if (belong[n] == belong[cur]) return false;
                    }
                }
            }
        }
        
        return true;
    }
};
```



```cpp
// cpp
// dfs

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> belong(n, -1);
        vector<bool> vis(n);
        
        for (int i = 0; i < n; ++i) {
            if (belong[i] != -1) continue;
            vector<int> s;
            belong[i] = 0;
            s.push_back(i);

            while (!s.empty()) {
                int u = s.back();
                s.pop_back();
                if (vis[u]) continue;
                vis[u] = true;
                for (int v: graph[u]) {
                    if (belong[v] == -1) belong[v] = !belong[u];
                    else if (belong[v] == belong[u]) return false;
                    s.push_back(v);
                }
            }
        }
        return true;
    }
};
```

```cpp
// cpp
// union-find-set

class Solution {
public:

    int find(vector<int>& ufs, int x) {
        if (x == ufs[x]) return x;
        return ufs[x] = find(ufs, ufs[x]);
    }

    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> ufs(n);
        for (int i = 0; i < n; ++i) ufs[i] = i;

        for (int i = 0; i < n; ++i) {
            if (graph[i].empty()) continue;
            int p = find(ufs, i);
            int q = find(ufs, graph[i][0]);
            if (p == q) return false;

            for (int j = 1; j < graph[i].size(); ++j) {
                int r = find(ufs, graph[i][j]);
                if (r == p) return false;
                ufs[r] = q; 
            }
        }
        return true;
    }
};
```



```python
# python3
# union-find-set

class Solution:
    def find(self, ufs, x):
        if x == ufs[x]:
            return x
        ufs[x] = self.find(ufs, ufs[x])
        return ufs[x]
        
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        ufs = [i for i in range(n)]

        for i in range(n):
            if not graph[i]:
                continue
            p = self.find(ufs, i)
            q = self.find(ufs, graph[i][0])
            if p == q:
                return False
            for j in graph[i]:
                r = self.find(ufs, j)
                if r == p:
                    return False
                ufs[r] = q
        return True
```

