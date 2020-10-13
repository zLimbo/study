#### [[medium]24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

> 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
>
> **你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。
>
>  
>
> **示例:**
>
> ```
> 给定 1->2->3->4, 你应该返回 2->1->4->3.
> ```

```cpp
// cpp
// list

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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        
        ListNode *prev = new ListNode(), *cur = head, *succ = head->next;
        head = prev;

        while (succ) {
            cur->next = succ->next;
            succ->next = cur;
            prev->next = succ;

            prev = cur;
            cur = cur->next;
            if (!cur) break;
            succ = cur->next;
        }

        return head->next;
    }
};
```

