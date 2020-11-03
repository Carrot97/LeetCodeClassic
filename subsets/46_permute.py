"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


def permute(nums: list) -> list:
    ans = []

    def helper(first):
        if first == len(nums):
            ans.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            helper(first+1)
            nums[first], nums[i] = nums[i], nums[first]

    helper(0)
    return ans


print(permute([1,2,3]))
