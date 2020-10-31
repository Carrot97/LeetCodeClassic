"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标
和的路径。说明:叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 99.88% 92.84%
def pathSum(root: TreeNode, sum: int) -> list:
    unvisited = []
    ans = []
    if root:
        unvisited.append((root, [], sum))
    while unvisited:
        node, path, target = unvisited.pop()
        path.append(node.val)
        if node.val == target and not node.left and not node.right:
            ans.append(path)
        if node.right:
            # 注意深拷贝（但会占用大量额外空间，可能是测试用例问题效果还不错）
            unvisited.append((node.right, path.copy(), target - node.val))
        if node.left:
            unvisited.append((node.left, path.copy(), target - node.val))
    return ans


head = TreeNode(5)
head.left = TreeNode(4)
head.left.left = TreeNode(11)
head.left.left.left = TreeNode(7)
head.left.left.right = TreeNode(2)
head.right = TreeNode(8)
head.right.left = TreeNode(13)
head.right.right = TreeNode(4)
head.right.right.left = TreeNode(5)
head.right.right.right = TreeNode(1)

print(pathSum(None, 22))
