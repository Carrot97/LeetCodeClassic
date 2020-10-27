"""
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，
总共可最多替换k次。在执行上述操作后，找到包含重复字母的最长子串的长度。
注意:
字符串长度 和 k 不会超过104。

示例 1:
输入:
s = "ABAB", k = 2
输出:
4
解释:
用两个'A'替换为两个'B',反之亦然。
"""


def characterReplacement(s: str, k: int) -> int:
    voc = [0] * 26
    start, ans = 0, 0
    for end in range(len(s)):
        if voc[ord(s[end]) - 65] == 0:
            voc[ord(s[end]) - 65] = 1
        else:
            voc[ord(s[end]) - 65] += 1
        while end - start + 1 - max(voc) > k:
            voc[ord(s[start]) - 65] -= 1
            start += 1
        ans = max(ans, end - start + 1)
    return ans


print(characterReplacement("ABAB", 1))
