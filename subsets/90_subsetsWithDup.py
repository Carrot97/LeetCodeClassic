"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[[2],[1],[1,2,2],[2,2],[1,2],[]]
"""


def subsetsWithDup(nums: list) -> list:
    ans = []
    nums.sort()

    def helper(res, idx):
        ans.append(res)
        first = True
        for i in range(idx, len(nums)):
            if nums[i - 1] != nums[i] or first:
                helper(res + [nums[i]], i + 1)
                first = False

    helper([], 0)
    return ans


print(subsetsWithDup([1,2,2,2]))
