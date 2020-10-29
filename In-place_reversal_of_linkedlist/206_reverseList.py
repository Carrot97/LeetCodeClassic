"""
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
from listNode import ListNode


def reverseList(head: ListNode):
    if not head:
        return None
    pre = head
    head = head.next
    pre.next = None
    while head:
        nxt = head.next
        head.next = pre
        pre = head
        head = nxt
    return pre


head = ListNode(1)
p = head
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(5)

head = reverseList(head)

p = head
while p:
    print(p.val)
    p = p.next
