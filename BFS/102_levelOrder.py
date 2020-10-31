"""
给你一个二叉树，请你返回其按层序遍历得到的节点值。（即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> list:
    unvisited = []
    ans = []
    if root:
        unvisited.append([root])
    while unvisited:
        level = unvisited.pop(0)
        ans.append([node.val for node in level])
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            unvisited.append(next_level)
    return ans


def levelOrder2(root: TreeNode) -> list:
    unvisited = []
    ans = []
    if root:
        unvisited.append(root)
    while unvisited:
        size = len(unvisited)
        level = []
        for _ in range(size):
            node = unvisited.pop(0)
            if not node:
                continue
            level.append(node.val)
            unvisited.append(node.left)
            unvisited.append(node.right)
        if level:
            ans.append(level)
    return ans


head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

print(levelOrder(head))

