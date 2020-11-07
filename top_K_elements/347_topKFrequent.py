"""
给定一个非空的整数数组，返回其中出现频率前k高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
"""
import heapq


def topKFrequent(nums: list, k: int) -> list:
    voc = {}
    for n in nums:
        if n not in voc:
            voc[n] = 1
        else:
            voc[n] += 1
    count = 0
    heap = []
    for key, val in voc.items():
        if count < k:
            heapq.heappush(heap, (val, key))
            count += 1
        else:
            if val > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (val, key))
    return [kv[1] for kv in heap]


print(topKFrequent([1], 1))
