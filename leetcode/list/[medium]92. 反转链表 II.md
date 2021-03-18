#### [[medium]92. 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

> 给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。
>
>  
>
> **示例 1：**
>
> ![img](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)
>
> ```
> 输入：head = [1,2,3,4,5], left = 2, right = 4
> 输出：[1,4,3,2,5]
> ```
>
> **示例 2：**
>
> ```
> 输入：head = [5], left = 1, right = 1
> 输出：[5]
> ```
>
>  
>
> **提示：**
>
> - 链表中节点数目为 `n`
> - `1 <= n <= 500`
> - `-500 <= Node.val <= 500`
> - `1 <= left <= right <= n`
>
>  
>
> **进阶：** 你可以使用一趟扫描完成反转吗？



```cpp
// 穿针引线

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
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        // if (left == right) return head;
        ListNode *prev = new ListNode(0, head);
        int idx = 0;
        while (++idx < left) {
            prev = prev->next;
        }
        ListNode *cur = prev->next;

        while (++idx <= right) {
            ListNode* succ = cur->next;
            cur->next = succ->next;
            succ->next = prev->next;
            prev->next = succ;
        }

        return left != 1 ? head : prev->next;
    }
};
```

