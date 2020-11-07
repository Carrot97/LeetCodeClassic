"""
你有k个非递减排列的整数列表。找到一个最小区间，使得k个列表中的每个列表至少有一个数包含在其中。

示例 1：
输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释：
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
"""
import heapq


def smallestRange(nums: list) -> list:
    ans = [-1e8, 1e8]
    heap = [(n[0], i, 0) for i, n in enumerate(nums)]
    maxVal = max([n[0] for n in nums])
    heapq.heapify(heap)
    while True:
        minVal, row, idx = heapq.heappop(heap)
        if maxVal - minVal < ans[1] - ans[0]:
            ans = [minVal, maxVal]
        if idx == len(nums[row]) - 1:
            break
        heapq.heappush(heap, (nums[row][idx + 1], row, idx + 1))
        maxVal = max(maxVal, nums[row][idx + 1])
    return ans


print(smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
