#### [[hard]99. 恢复二叉搜索树](https://leetcode-cn.com/problems/recover-binary-search-tree/)

> 二叉搜索树中的两个节点被错误地交换。
>
> 请在不改变其结构的情况下，恢复这棵树。
>
> ```shell
> 示例 1:
> 
> 输入: [1,3,null,null,2]
> 
>    1
>   /
>  3
>   \
>    2
> 
> 输出: [3,1,null,null,2]
> 
>    3
>   /
>  1
>   \
>    2
> 示例 2:
> 
> 输入: [3,1,4,null,null,2]
> 
>   3
>  / \
> 1   4
>    /
>   2
> 
> 输出: [2,1,4,null,null,3]
> 
>   2
>  / \
> 1   4
>    /
>   3
> ```
>
> **进阶:**
>
> - 使用 O(*n*) 空间复杂度的解法很容易实现。
> - 你能想出一个只使用常数空间的解决方案吗？
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/recover-binary-search-tree
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
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
    TreeNode *last = nullptr;
    TreeNode *tn1 = nullptr;
    TreeNode *tn2 = nullptr;

    void dfs(TreeNode* root) {
        if (!root) return;
        dfs(root->left);
        if (last && last->val > root->val) {
            if (!tn1) tn1 = last;
            tn2 = root;
        }
        last = root;
        dfs(root->right);
    }

    void recoverTree(TreeNode* root) {
        dfs(root);
        if (tn1 && tn2) swap(tn1->val, tn2->val);
    }
};
```



```cpp
// cpp
// Morris 遍历

class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode *x = nullptr, *y = nullptr, *prev = nullptr;
        while (root) {
            if (root->left) {
                TreeNode* succ = root->left;
                while (succ->right && succ->right != root)
                    succ = succ->right;
                if (!(succ->right)) {
                    succ->right = root;
                    root = root->left;
                    continue;
                }
                succ->right = nullptr;
            }
            if (prev && prev->val > root->val) {
                if (!x) x = prev;
                y = root;
            }
            prev = root;
            root = root->right;
        }
        swap(x->val, y->val);
    }
};
```



```python
# python
# Morris 遍历

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x, y, prev = None, None, None
        while root:
            if root.left:
                succ = root.left
                while succ.right and succ.right != root:
                    succ = succ.right
                if not succ.right:
                    succ.right = root
                    root = root.left
                    continue
                succ.right = None
            # 访问
            if prev and prev.val > root.val:
                if not x:
                    x = prev
                y = root
            prev = root
            root = root.right
        x.val, y.val = y.val, x.val
```

