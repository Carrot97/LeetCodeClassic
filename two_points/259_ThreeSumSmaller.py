"""
Given an array of n integers nums and a target, find the number of
index triplets i, j, k with 0 <= i < j < k < n that satisfy the
condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.
Return 2. Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]
"""


def ThreeSumSmaller(nums: list, target: int) -> int:
    n = len(nums)
    nums.sort()
    ans = 0
    for first in range(n - 2):
        if nums[first] > target:
            break
        third = n - 1
        new_target = target - nums[first]
        for second in range(first + 1, n - 1):
            while second < third and nums[second] + nums[third] >= new_target:
                third -= 1
            if second == third:
                break
            ans += third - second
    return ans


print(ThreeSumSmaller([-2, 0, 1, 3], 2))
