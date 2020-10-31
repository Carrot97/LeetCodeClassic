"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明:叶子节点是指没有子节点的节点。

示例:
给定二叉树[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度 2.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root: TreeNode) -> int:
    unvisited = []
    if root:
        unvisited.append([root])
    idx = 0
    while unvisited:
        idx += 1
        level = unvisited.pop(0)
        next_level = []
        for node in level:
            if not node.left and not node.right:
                return idx
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            unvisited.append(next_level)
    return idx


def minDepth2(root: TreeNode) -> int:
    unvisited = []
    if root:
        unvisited.append(root)
    ans = 0
    while unvisited:
        ans += 1
        for _ in range(len(unvisited)):
            node = unvisited.pop(0)
            if not node.left and not node.right:
                return ans
            if node.left:
                unvisited.append(node.left)
            if node.right:
                unvisited.append(node.right)
    return ans


head = TreeNode(3)
head.left = TreeNode(9)
# head.left.left = TreeNode(1)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

print(minDepth2(head))
