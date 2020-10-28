"""
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（
索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针法（快指针每次走两格，慢指针每次走一格），O(1)空间复杂度
def hasCycle(head):
    if not head:
        return False
    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


# 使用额外O(n)空间(哈希表)，降低时间复杂度
# 但考虑到哈希运算的开销，可能无法显著降低时间复杂度
def best_solution(head):
    voc = set()
    while head:
        if head in voc:
            return True
        voc.add(head)
        head = head.next
    return False



















