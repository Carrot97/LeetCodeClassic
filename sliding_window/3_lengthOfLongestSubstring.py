"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
示例1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
"""

# 很久之前写的
# def lengthOfLongestSubstring(s: str) -> int:
#     m = len(s)
#     if m <= 1:
#         return m
#     s += s[-1]
#     m += 1
#     voc = {}
#     ans, count, i = 0, 0, 0
#     while i + count < m:
#         val = s[i + count]
#         if val not in voc.keys():
#             voc[val] = i + count
#             count += 1
#         else:
#             ans = max(count, ans)
#             i = voc[val] + 1
#             voc = {}
#             count = 0
#     return ans


def lengthOfLongestSubstring2(s: str) -> int:
    n = len(s)
    voc = [-1] * 26
    start = ans = 0
    for end in range(n):
        if voc[ord(s[end]) - 97] == -1:
            voc[ord(s[end]) - 97] = end
        else:
            for i in range(start, voc[ord(s[end]) - 97]):
                voc[i] = -1
            start = voc[ord(s[end]) - 97] + 1
            voc[ord(s[end]) - 97] = end
        ans = max(ans, end - start + 1)
    return ans


print(lengthOfLongestSubstring2(" "))
