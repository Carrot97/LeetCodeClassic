"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[ 1->4->5,
  1->3->4,
  2->6 ]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
"""
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list) -> ListNode:
    heap = []
    ans = p = ListNode(0)
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i))
    while heap:
        _, idx = heapq.heappop(heap)
        p.next = lists[idx]
        p = p.next
        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(heap, (lists[idx].val, idx))
    return ans.next


head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
head3 = ListNode(2)
head3.next = ListNode(6)

head = mergeKLists([None])
while head:
    print(head.val)
    head = head.next
