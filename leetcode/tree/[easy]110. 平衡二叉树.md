#### [[easy]110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

> 给定一个二叉树，判断它是否是高度平衡的二叉树。
>
> 本题中，一棵高度平衡二叉树定义为：
>
> 一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过1。
>
> ```python
> 示例 1:
> 
> 给定二叉树 [3,9,20,null,null,15,7]
> 
>     3
>    / \
>   9  20
>     /  \
>    15   7
> 返回 true 。
> 
> 示例 2:
> 
> 给定二叉树 [1,2,2,3,3,null,null,4,4]
> 
>        1
>       / \
>      2   2
>     / \
>    3   3
>   / \
>  4   4
> 返回 false 。
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/balanced-binary-tree
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
# python3
# dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(root):
            if not root:
                return 0
            lch = helper(root.left)
            if lch == -1:
                return -1
            rch = helper(root.right)
            if rch == -1:
                return -1
            if not (-1 <= lch - rch <= 1):
                return -1
            return 1 + max(lch, rch)

        return False if helper(root) == -1 else True
```

