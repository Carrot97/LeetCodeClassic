"""
给定一个包含 0, 1, 2, ..., n中n个数的序列，找出 0 .. n中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8
"""


# 圈排序算法
def missingNumber1(nums: list):
    # 依次遍历所有元素，将该元素-1作为索引，将该索引上的数字置为负表示此位置上的数字存在。
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] > 0:
            nums[idx] *= -1
    # 找到空位上的（正数）数字即为答案
    for i, n in enumerate(nums):
        if n > 0:
            return i + 1
    return -1


# 哈希表算法
def missingNumber2(nums: list):
    voc = set()
    for n in nums:
        voc.add(n)
    for i in range(len(nums) + 1):
        if i not in voc:
            return i


print(missingNumber1([3, 0, 1]))
