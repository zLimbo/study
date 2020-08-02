#### [[medium]114. 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)

> 给定一个二叉树，[原地](https://baike.baidu.com/item/原地算法/8010757)将它展开为一个单链表。
>
> 例如，给定二叉树
>
> ```shell
>   	1
>    / \
>   2   5
>  / \   \
> 3   4   6
> ```
>
> 将其展开为：
>
> ```shell
> 1
>  \
>   2
>    \
>     3
>      \
>       4
>        \
>         5
>          \
>           6
> ```



```python
# python3
# stack + 前序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        if root:
            stack.append(root)
        proTn = TreeNode()
        while stack:
            tn = stack.pop()
            if tn.right:
                stack.append(tn.right)
            if tn.left:
                stack.append(tn.left)
            proTn.right = tn
            tn.left = None
            proTn = tn
```



```cpp
// cpp
// 前驱节点

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
    void flatten(TreeNode* root) {
        TreeNode* tn = root;
        while (tn) {
            if (tn->left) {
                TreeNode* prev = tn->left;
                while (prev->right) {
                    prev = prev->right;
                }
                prev->right = tn->right;
                tn->right = tn->left;
                tn->left = nullptr;
            }
            tn = tn->right;
        }
    }
};
```



```cpp
// cpp
// 递归

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
    TreeNode* next = nullptr;
    void flatten(TreeNode* root) {
        if (!root) {
            return;
        }
        flatten(root->right);
        flatten(root->left);
        root->right = next;
        root->left = nullptr;
        next = root;
    }
};
```

