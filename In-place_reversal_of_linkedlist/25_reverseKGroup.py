"""
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当k= 2 时，应当返回: 2->1->4->3->5
当k= 3 时，应当返回: 3->2->1->4->5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    hair = ListNode(0)
    hair.next = head
    left = hair
    while head:
        tail = left
        # 单独寻找尾结点
        for i in range(k):
            tail = tail.next
            if not tail:
                return hair.next
        right = tail.next
        pre = head
        cur = head.next
        while pre != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        head.next = right
        left.next = tail
        left = head
        head = right
    return hair.next


head = ListNode(1)
p = head
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(5)

head = reverseKGroup(head, 2)

p = head
while p:
    print(p.val)
    p = p.next
