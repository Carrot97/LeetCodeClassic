"""
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。如果pos是-1，则在该链表中没有环。注意，
pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 哈希表实现
def detectCycle(head: ListNode) -> ListNode:
    voc = set()
    while head:
        if head in voc:
            return head
        voc.add(head)
        head = head.next
    return None


# 快慢指针实现
def detectCycle2(head: ListNode) -> ListNode:
    if not head:
        return None
    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            ptr = head
            while ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None


