"""
数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""


def generateParenthesis(n: int) -> list:
    ans = []

    # count为未被平衡的括号数量（正为左括号，负为右括号）
    def helper(res, count):
        # 不允许出现未被平衡的右括号
        # 不允许出现未被平衡的左括号超过n个
        if count < 0 or count > n:
            return
        if len(res) == 2 * n:
            # 必须平衡才能加入最终结果
            if count == 0:
                ans.append(''.join(res))
            return
        helper(res + ["("], count + 1)
        helper(res + [")"], count - 1)

    helper([], 0)
    return ans


print(generateParenthesis(3))
