"""
给定一个字符串S，通过将字符串S中的每个字母转变大小写，
我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]
"""


def letterCasePermutation(S: str):
    ans = []
    # 先将所有字母转换为小写，避免回溯时麻烦
    S = list(S.lower())

    def helper(first: int):
        if first == len(S):
            ans.append(''.join(S))
            return
        if S[first].isalpha():
            S[first] = S[first].upper()
            helper(first + 1)
            S[first] = S[first].lower()
        helper(first + 1)

    helper(0)
    return ans


print(letterCasePermutation("C"))
