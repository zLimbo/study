#### [[medium]109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)

> 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
>
> 本题中，一个高度平衡二叉树是指一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过 1。
>
> ```python
> 示例:
> 
> 给定的有序链表： [-10, -3, 0, 5, 9],
> 
> 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
> 
>       0
>      / \
>    -3   9
>    /   /
>  -10  5
> 
> ```
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> vals;
        while (head) {
            vals.push_back(head->val);
            head = head->next;
        }
        return buildTree(vals, 0, vals.size() - 1);
    }

    TreeNode* buildTree(vector<int>& vals, int low, int high) {
        if (low > high) return nullptr;
        int mid = ((high - low) >> 1) + low;
        return new TreeNode(vals[mid], 
                buildTree(vals, low, mid - 1), 
                buildTree(vals, mid + 1, high));
    }
};
```



```python
# python3
# 快慢指针

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        def getMid(left, right):
            slow, fast = left, left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def buildTree(left, right):
            if left == right:
                return None
            mid = getMid(left, right)
            return TreeNode(mid.val, buildTree(left, mid), buildTree(mid.next, right))
        
        return buildTree(head, None)
```



```python
# python3
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        def getLength(head):
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def buildTree(left, right):
            if left > right:
                return None
            mid = (left + right) >> 1
            nonlocal head
            left = buildTree(left, mid - 1)
            tn = TreeNode(head.val, left)
            head = head.next
            tn.right = buildTree(mid + 1, right)
            return tn
            
        length = getLength(head)
        return buildTree(0, length - 1)
```

