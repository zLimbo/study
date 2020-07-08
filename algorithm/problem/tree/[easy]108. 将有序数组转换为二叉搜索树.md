#### [[easy]108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

> 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
>
> 本题中，一个高度平衡二叉树是指一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过 1。



```cpp
// cpp
// tree

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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        
        return buildTree(nums, 0, nums.size());
    }

    TreeNode* buildTree(vector<int>& nums, int lo, int hi) {
        if (lo >= hi) return nullptr;
        int mi = lo + ((hi - lo) >> 1);
        TreeNode* ret = new TreeNode(nums[mi]);
        ret->left = buildTree(nums, lo, mi);
        ret->right = buildTree(nums, mi+1, hi);
        return ret;
    }
};
```

