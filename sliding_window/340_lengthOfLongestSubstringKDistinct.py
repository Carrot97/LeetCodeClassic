"""
Given a string, find the length of the longest substring T that
contains at most k distinct characters.
For example, Given s = “eceba” and k = 2,
T is "ece" which its length is 3.
"""


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    voc = {}
    start, ans, distinct = 0, 0, 0
    for end in range(len(s)):
        if s[end] not in voc:
            voc[s[end]] = 1
            distinct += 1
        else:
            voc[s[end]] += 1
        if distinct > k:
            while True:
                voc[s[start]] -= 1
                start += 1
                if voc[s[start - 1]] == 0:
                    distinct -= 1
                    break
        ans = max(ans, end - start + 1)
    return ans

print(lengthOfLongestSubstringKDistinct("abacc", 2))