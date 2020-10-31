"""
给你一个二叉树的根节点root。设根节点位于二叉树的第 1 层，而根节点的子节点位于
第 2 层，依此类推。请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，
并返回其中最小 的那个。

示例 1：
输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root: TreeNode) -> int:
    unvisited = []
    max_sum = -1e8
    # idx记录层号
    idx, ans = 0, 0
    if root:
        unvisited.append([root])
    while unvisited:
        idx += 1
        level = unvisited.pop(0)
        next_level = []
        cur_sum = sum([node.val for node in level])
        if cur_sum > max_sum:
            ans = idx
            max_sum = cur_sum
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            unvisited.append(next_level)
    return ans


head = TreeNode(1)
head.left = TreeNode(7)
head.right = TreeNode(0)
head.left.left = TreeNode(7)
head.left.right = TreeNode(-8)

print(maxLevelSum(None))
