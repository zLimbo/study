#### [[easy]112. 路径总和](https://leetcode-cn.com/problems/path-sum/)



> 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
>
> 说明: 叶子节点是指没有子节点的节点。
>
> 示例: 
> 给定如下二叉树，以及目标和 sum = 22，
>
>               5
>              / \
>             4   8
>            /   / \
>           11  13  4
>          /  \      \
>         7    2      1
> 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/path-sum
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
// cpp
// tree
// 队列

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        queue<TreeNode*> q;
        queue<int> sq;
        if (root) {
            q.push(root);
            sq.push(root->val);
        }

        while (!q.empty()) {
            TreeNode* cur = q.front(); q.pop();
            int s = sq.front(); sq.pop();
            if (!(cur->left) && !(cur->right)) {
                if (s == sum) { 
                    return true;
                }
                continue;
            }
            if (cur->left) {
                q.push(cur->left);
                sq.push(s + cur->left->val);
            }
            if (cur->right) {
                q.push(cur->right);
                sq.push(s + cur->right->val);
            }
            
        }
        return false;
    }
};
```



```cpp
// cpp
// tree
// 递归

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root) {
            return false;
        }
        sum -= root->val;
        if (!root->left && !root->right) {
            return sum == 0;
        }
        return hasPathSum(root->left, sum) || hasPathSum(root->right, sum);
    }
};
```



```python
# python
# tree
# 队列

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        tq = collections.deque()
        vq = collections.deque()
        if root:
            tq.append(root)
            vq.append(root.val)
        while tq:
            t = tq.popleft()
            v = vq.popleft()
            if not t.left and not t.right:
                if v == sum:
                    return True
                continue
            if t.left:
                tq.append(t.left)
                vq.append(v + t.left.val)
            if t.right:
                tq.append(t.right)
                vq.append(v + t.right.val)
        return False
```



```python
# python
# tree
# 递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

