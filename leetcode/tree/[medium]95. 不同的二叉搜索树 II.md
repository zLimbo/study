#### [[medium]95. 不同的二叉搜索树 II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)

> 给定一个整数 *n*，生成所有由 1 ... *n* 为节点所组成的 **二叉搜索树** 。
>
> **示例：**
>
> ```shell
> 输入：3
> 输出：
> [
>   [1,null,3,2],
>   [3,2,null,1],
>   [3,1,null,null,2],
>   [2,1,3],
>   [1,null,2,null,3]
> ]
> 解释：
> 以上的输出对应以下 5 种不同结构的二叉搜索树：
> 
>    1         3     3      2      1
>     \       /     /      / \      \
>      3     2     1      1   3      2
>     /     /       \                 \
>    2     1         2                 3
> 
> ```
>
> **提示：**
>
> - `0 <= n <= 8`
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// recursion

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n <= 0) return vector<TreeNode*>();
        return generateTrees(1, n);
    }

    vector<TreeNode*> generateTrees(int lo, int hi) {
        vector<TreeNode*> ret;

        for (int i = lo; i <= hi; ++i) {
            vector<TreeNode*> left = generateTrees(lo, i-1);
            vector<TreeNode*> right = generateTrees(i+1, hi);
            for (TreeNode* lt: left) {
                for (TreeNode* rt: right) {
                    ret.push_back(new TreeNode(i, lt, rt));
                }
            }
        }
        if (ret.empty()) ret.push_back(nullptr);
        return ret;
    }
};
```



```python
# python3
# recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def aux(lo, hi):
            if lo > hi:
                return [None,]
            ret = []
            for i in range(lo, hi+1):
                left = aux(lo, i-1)
                right = aux(i+1, hi)
                ret.extend([TreeNode(i, lc, rc) for lc in left for rc in right])
            return ret
        return aux(1, n) if n else []
```



```java
// java
// recursion

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (0 == n) return new ArrayList<TreeNode>();
        return generateTrees(1, n);
    }

    private List<TreeNode> generateTrees(int lo, int hi) {
        List<TreeNode> ret = new ArrayList<TreeNode>();
        for (int i = lo; i <= hi; ++i) {
            List<TreeNode> left = generateTrees(lo, i-1);
            List<TreeNode> right = generateTrees(i+1, hi);
            for (TreeNode lc: left) {
                for (TreeNode rc: right) {
                    ret.add(new TreeNode(i, lc, rc));
                }
            }
        }
        if (ret.isEmpty()) ret.add(null);
        return ret;
    }
}
```

