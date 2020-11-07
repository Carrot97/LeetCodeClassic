"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:
输入:
"tree"
输出:
"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
"""
import heapq


def frequencySort(s: str):
    voc = {}
    for c in s:
        if c not in voc:
            voc[c] = 1
        else:
            voc[c] += 1
    heap = []
    for k, v in voc.items():
        heapq.heappush(heap, (-v, k))
    ans = []
    while heap:
        v, k = heapq.heappop(heap)
        for _ in range(-v):
            ans.append(k)
    return ''.join(ans)


print(frequencySort("Aabb"))
