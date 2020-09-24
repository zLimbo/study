#### [[easy]501. 二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)

> 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
>
> 假定 BST 有如下定义：
>
> - 结点左子树中所含结点的值小于等于当前结点的值
> - 结点右子树中所含结点的值大于等于当前结点的值
> - 左子树和右子树都是二叉搜索树
>
> 例如：
> 给定 BST `[1,null,2,2]`,
>
> ```
>    1
>     \
>      2
>     /
>    2
> ```
>
> `返回[2]`.
>
> **提示**：如果众数超过1个，不需考虑输出顺序
>
> **进阶：**你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）



```cpp
// cpp

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
    vector<int> findMode(TreeNode* root) {
        if (root == nullptr) return {};
        vector<int> ans;
        int val = 0, cnt = 0, max_cnt = 0;
        TreeNode* tn = root;
        while (root) {
            if (root->left) {
                TreeNode* succ = root->left;
                while (succ->right && succ->right != root) {
                    succ = succ->right;
                }
                if (succ->right == nullptr) {
                    succ->right = root;
                    root = root->left;
                    continue;
                } else {
                    succ->right = nullptr;
                }
            }

            if (val == root->val) {
                ++cnt;
            }
            else {
                if (cnt > max_cnt) {
                    max_cnt = cnt;
                    ans.clear();
                    ans.push_back(val);
                }
                else if (cnt == max_cnt) {
                    ans.push_back(val);
                }
                cnt = 1;
                val = root->val;
            }
            root = root->right;
        }
        if (cnt > max_cnt) {
            max_cnt = cnt;
            cnt = 1;
            ans.clear();
            ans.push_back(val);
        }
        else if (cnt == max_cnt) {
            ans.push_back(val);
        }
        return ans;
    }
};
```

