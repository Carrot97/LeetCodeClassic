"""
Given an array of integers of size ‘n’.Our aim is to calculate the
maximum sum of ‘k’ consecutive elements in the array.
"""


def MaximumSumSubarrayOfSizeK(nums: list, k: int) -> int:
    n = len(nums)
    if n < k:
        return 0
    i, j = 0, k - 1
    ans = cur_sum = sum(nums[i:k])
    while j < n - 1:
        j += 1
        cur_sum += nums[j] - nums[i]
        i += 1
        ans = max(ans, cur_sum)
    return ans


print(MaximumSumSubarrayOfSizeK([2, 3], 3))
