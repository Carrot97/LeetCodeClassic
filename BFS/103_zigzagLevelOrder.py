"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。
即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行

例如：
给定二叉树[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzagLevelOrder(root: TreeNode) -> list:
    unvisited = []
    ans = []
    # 输出顺序指示器
    order = 1
    if root:
        unvisited.append([root])
    while unvisited:
        level = unvisited.pop(0)
        next_level = []
        ans.append([node.val for node in level[::order]])
        order *= -1
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            unvisited.append(next_level)
    return ans


head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

print(zigzagLevelOrder(None))
