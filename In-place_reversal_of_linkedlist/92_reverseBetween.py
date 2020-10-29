"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    # 向链表头部插入哨兵，解决从头翻转问题
    cur = ListNode(0)
    cur.next = head
    head = cur
    idx = 0
    while idx < m - 1:
        cur = cur.next
        idx += 1
    # left为左侧不需翻转链表的末尾，等待需要翻转链表部分的头部链接
    left = cur
    # tail为需要翻转链表部分的尾部，需要连接右侧不需翻转链表的头部
    # 以下同206题
    tail = pre = cur.next
    cur = pre.next
    idx += 1
    while idx < n:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
        idx += 1
    # 此时pre即为head：需要翻转链表部分的头部
    left.next = pre
    # 此时cur即为right：右侧不需翻转链表的头部
    tail.next = cur
    return head.next


head = ListNode(1)
p = head
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(5)

head = reverseBetween(head, 2, 5)

p = head
while p:
    print(p.val)
    p = p.next
