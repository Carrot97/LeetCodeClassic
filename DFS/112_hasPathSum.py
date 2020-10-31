"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。
说明:叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
def hasPathSum1(root: TreeNode, sum: int):
    if not root:
        return False
    if not root.left and not root.right:
        # 将return展开可节约时间（很奇怪）
        # return root.val == sum
        if root.val == sum:
            return True
        else:
            return False
    return hasPathSum1(root.left, sum - root.val) or hasPathSum1(root.right, sum - root.val)


# DFS
def hasPathSum2(root: TreeNode, sum: int):
    unvisited = []
    if root:
        unvisited.append((root, sum))
    while unvisited:
        node, target = unvisited.pop()
        if node.val == target and not node.left and not node.right:
            return True
        if node.right:
            unvisited.append((node.right, target - node.val))
        if node.left:
            unvisited.append((node.left, target - node.val))
    return False


head = TreeNode(5)
head.left = TreeNode(4)
head.left.left = TreeNode(11)
head.left.left.left = TreeNode(7)
head.left.left.right = TreeNode(2)
head.left.left.right.left = TreeNode(3)
head.right = TreeNode(8)
head.right.left = TreeNode(13)
head.right.right = TreeNode(4)
head.right.right.right = TreeNode(1)

print(hasPathSum2(None, 22))
