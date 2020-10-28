"""
给定数组中只有“1”，“2”，“3”三种数字，且个数不等
排序
最终结果的顺序为：所有的1在前，所有的2在中间，所有的3在后
如：原数组：1232313231，排序后：1112223333
"""


def DutchNationalFlagProblem(nums: list):
    # 三向快排算法
    lo, i, hi = 0, 0, len(nums) - 1
    while i <= hi:
        if nums[i] == 1:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
            i += 1
        elif nums[i] == 3:
            nums[hi], nums[i] = nums[i], nums[hi]
            hi -= 1
        else:
            i += 1
    return nums


print(DutchNationalFlagProblem([1, 1, 2, 1, 3, 2, 1, 2]))
