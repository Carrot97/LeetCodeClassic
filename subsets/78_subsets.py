"""
给定一组不含重复元素的整数数组nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
"""


# 迭代
def subsets(nums: list) -> list:
    ans = [[]]
    for n in nums:
        size = len(ans)
        for a in ans[:size]:
            ans.append(a + [n])
    return ans


# 深搜回溯
def subsets(nums: list) -> list:
    ans = []

    def helper(res, idx):
        ans.append(res)
        for i in range(idx, len(nums)):
            helper(res + [nums[i]], i + 1)

    helper([], 0)
    return ans


print(subsets([1, 2, 3]))
