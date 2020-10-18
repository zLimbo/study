#### [[medium]19. 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

> 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
>
> 示例：
>
> 给定一个链表: 1->2->3->4->5, 和 n = 2.
>
> 当删除了倒数第二个节点后，链表变为 1->2->3->5.
> 说明：
>
> 给定的 n 保证是有效的。
>
> 进阶：
>
> 你能尝试使用一趟扫描实现吗？

```cpp
// cpp
// 双指针

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode * fast = head, * slow = head;
        ListNode * prev = new ListNode(), * ret = prev;
        prev->next = head;
        while (n--) {
            fast = fast->next;
        }
        while (fast) {
            fast = fast->next;
            prev = slow;
            slow = slow->next;
        }
        prev->next = slow->next;
        delete slow;
        return ret->next;
    }
};
```



