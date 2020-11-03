""""
给定一个二叉树，我们称从根节点到任意叶节点的任意路径中的节点值所构成的序列为该二叉树的一个 “有效序列” 。
检查一个给定的序列是否是给定二叉树的一个 “有效序列” 。
我们以整数数组 arr 的形式给出这个序列。
从根节点到任意叶节点的任意路径中的节点值所构成的序列都是这个二叉树的 “有效序列” 。
输入：root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
输出：true
解释：
路径 0 -> 1 -> 0 -> 1 是一个“有效序列”（图中的绿色节点）。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidSequence(root: TreeNode, arr: list) -> bool:
    found = False

    def helper(p: TreeNode, arr: list, idx: int):
        nonlocal found
        if not p or found or idx == len(arr):
            return
        if p.val == arr[idx]:
            if not p.left and not p.right and idx == len(arr) - 1:
                found = True
                return
            helper(p.left, arr, idx+1)
            helper(p.right, arr, idx+1)

    helper(root, arr, 0)
    return found


head = TreeNode(0)
head.left = TreeNode(1)
head.right = TreeNode(0)
head.left.left = TreeNode(0)
head.left.right = TreeNode(1)
head.left.left.right = TreeNode(1)
head.left.right.left = TreeNode(0)
head.left.right.right = TreeNode(0)
head.right.left = TreeNode(0)

print(isValidSequence(head, [0,1,1,0]))

