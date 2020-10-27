"""
Given an array nums and a target value k, find the maximum length of
a subarray that sums to k. If there isn't one, return 0 instead.
"""


def MaximumSizeSubarraySumEqualsK(nums: list, k: int) -> int:
    voc = {0: -1}
    cur_sum = ans = 0
    for i, num in enumerate(nums):
        cur_sum += num
        if num not in voc:
            voc[num] = i
        if cur_sum - k in voc:
            ans = max(ans, i - voc[cur_sum - k])
    return ans


print(MaximumSizeSubarraySumEqualsK([-2, -1, 2, 1], 1))
