"""
给定一个整数数组a，其中1≤a[i]≤n（n为数组长度）, 其中有些元素出现两次而其他元素
出现一次。找到所有出现两次的元素。

示例：
输入:
[4,3,2,7,8,2,3,1]
输出:
[2,3]
"""


# 要求不使用额外空间
def findDuplicates(nums: list) -> list:
    ans = []
    for n in nums:
        if nums[abs(n) - 1] > 0:
            nums[abs(n) - 1] *= -1
        else:
            ans.append(abs(n))
    return ans


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
