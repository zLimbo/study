#### [[medium]133. 克隆图](https://leetcode-cn.com/problems/clone-graph/)

> 给你无向 **[连通](https://baike.baidu.com/item/连通图/6460995?fr=aladdin)** 图中一个节点的引用，请你返回该图的 [**深拷贝**](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)（克隆）。
>
> 图中的每个节点都包含它的值 `val`（`int`） 和其邻居的列表（`list[Node]`）。
>
> ```java
> class Node {
>     public int val;
>     public List<Node> neighbors;
> }
> ```
>
> **测试用例格式：**
>
> 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（`val = 1`），第二个节点值为 2（`val = 2`），以此类推。该图在测试用例中使用邻接列表表示。
>
> **邻接列表** 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
>
> 给定节点将始终是图中的第一个节点（值为 1）。你必须将 **给定节点的拷贝** 作为对克隆图的引用返回。
>
> <img src="[medium]133. 克隆图.assets/133_clone_graph_question.png" alt="img" style="zoom: 25%;" />
>
> ```shell
> 输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
> 输出：[[2,4],[1,3],[2,4],[1,3]]
> 解释：
> 图中有 4 个节点。
> 节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
> 节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
> 节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
> 节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
> ```
>
> **提示：**
>
> 1. 节点数不超过 100 。
> 2. 每个节点值 `Node.val` 都是唯一的，`1 <= Node.val <= 100`。
> 3. 无向图是一个[简单图](https://baike.baidu.com/item/简单图/1680528?fr=aladdin)，这意味着图中没有重复的边，也没有自环。
> 4. 由于图是无向的，如果节点 *p* 是节点 *q* 的邻居，那么节点 *q* 也必须是节点 *p* 的邻居。
> 5. 图是连通图，你可以从给定节点访问到所有节点。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/clone-graph
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
# python3
# dfs

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nds = dict()

        def clone(node):
            if node in nds:
                return nds[node]
            ret = nds[node] = Node(node.val)
            for ngr in node.neighbors:
                ret.neighbors.append(clone(ngr))
            return ret
        
        return clone(node)
```



```cpp
// cpp
// dfs

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
public:
    unordered_map<Node*, Node*> nds;

    Node* clone(Node* node) {
        if (nds.find(node) != nds.end()) return nds[node];
        Node* ret = nds[node] = new Node(node->val);
        for (Node* neg: node->neighbors)
            ret->neighbors.push_back(cloneGraph(neg));
        return ret;
    }

    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        return clone(node);
    }
};
```



```java
// java
// bfs

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        HashMap<Node, Node> hmp = new HashMap();
        LinkedList<Node> queue = new LinkedList<Node>();
        queue.add(node);
        hmp.put(node, new Node(node.val));

        while (!queue.isEmpty()) {
            Node nd = queue.remove();
            Node nnd = hmp.get(nd);
            for (Node ngr: nd.neighbors) {
                if (!hmp.containsKey(ngr)) {
                    hmp.put(ngr, new Node(ngr.val));
                    queue.add(ngr);
                }
                nnd.neighbors.add(hmp.get(ngr));
            }
        }
        return hmp.get(node);
    }
}
```

