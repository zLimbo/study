#### [[medium]332. 重新安排行程](https://leetcode-cn.com/problems/reconstruct-itinerary/)

> 给定一个机票的字符串二维数组 `[from, to]`，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
>
> **说明:**
>
> 1. 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
> 2. 所有的机场都用三个大写字母表示（机场代码）。
> 3. 假定所有机票至少存在一种合理的行程。
>
> ```python
> 示例 1:
> 
> 输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
> 输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
> 示例 2:
> 
> 输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
> 输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
> 解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/reconstruct-itinerary
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

> 我们化简本题题意：给定一个 nn 个点 mm 条边的图，要求从指定的顶点出发，经过所有的边恰好一次（可以理解为给定起点的「一笔画」问题），使得路径的字典序最小。
>
> 这种「一笔画」问题与欧拉图或者半欧拉图有着紧密的联系，下面给出定义：
>
> - 通过图中所有边恰好一次且行遍所有顶点的通路称为欧拉通路。
>
> - 通过图中所有边恰好一次且行遍所有顶点的回路称为欧拉回路。
>
> - 具有欧拉回路的无向图称为欧拉图。
>
> - 具有欧拉通路但不具有欧拉回路的无向图称为半欧拉图。
>
>
> 因为本题保证至少存在一种合理的路径，也就告诉了我们，这张图是一个欧拉图或者半欧拉图。我们只需要输出这条欧拉通路的路径即可。
>
> 如果没有保证至少存在一种合理的路径，我们需要判别这张图是否是欧拉图或者半欧拉图，具体地：
>
> - 对于无向图 GG，GG 是欧拉图当且仅当 GG 是连通的且没有奇度顶点。
>
> - 对于无向图 GG，GG 是半欧拉图当且仅当 GG 是连通的且 GG 中恰有 22 个奇度顶点。
>
> - 对于有向图 GG，GG 是欧拉图当且仅当 GG 的所有顶点属于同一个强连通分量且每个顶点的入度和出度相同。
>
> - 对于有向图 GG，GG 是半欧拉图当且仅当 GG 的所有顶点属于同一个强连通分量且
>   - 恰有一个顶点的出度与入度差为 11；
>   - 恰有一个顶点的入度与出度差为 11；
>   - 所有其他顶点的入度和出度相同。
>
> 作者：LeetCode-Solution
> 链接：https://leetcode-cn.com/problems/reconstruct-itinerary/solution/zhong-xin-an-pai-xing-cheng-by-leetcode-solution/
> 来源：力扣（LeetCode）
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```cpp
// python
// 欧拉回路/欧拉通路

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(lambda : [])
        for edge in tickets:
            adj[edge[0]].append(edge[1])
        for k in adj.keys():
            adj[k].sort(reverse=True)
        ans = []

        def dfs(cur):
            while adj[cur]:
                dfs(adj[cur].pop())
            ans.append(cur)

        dfs('JFK')
        ans.reverse()
        return ans
```

```cpp
// cpp
//

// cpp
//

class Solution {
public:
    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> adj;
    vector<string> ans;

    void dfs(const string& cur) {
        while (!adj[cur].empty()) {
            string next = adj[cur].top();
            adj[cur].pop();
            dfs(next);
        }
        ans.emplace_back(move(cur));
    }

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for (auto &edge: tickets) {
            adj[edge[0]].push(edge[1]);
        }
        dfs("JFK");
        reverse(ans.begin(), ans.end());

        return ans;
    }
};
```



```cpp
// cpp
//

class Solution {
public:
    unordered_map<string, vector<string>> adj;
    vector<string> ans;

    void dfs(string&& cur) {
        while (!adj[cur].empty()) {
            string&& next = move(adj[cur].back());
            adj[cur].pop_back();
            dfs(move(next));
        }
        ans.emplace_back(move(cur));
    }

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for (auto &edge: tickets) {
            adj[edge[0]].push_back(edge[1]);
        }
        for (auto &x: adj) {
            sort(x.second.begin(), x.second.end(), 
                    [](const string& x, const string& y) { return x > y; });
        }

        dfs("JFK");
        reverse(ans.begin(), ans.end());

        return ans;
    }
};
```

