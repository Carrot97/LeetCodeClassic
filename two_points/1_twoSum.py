"""
题目：
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的
那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""

nums = [2, 7, 11, 13]
target = 9


# 排序后使用首尾递进式查找  ！！重要！！
def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # lambda 将以此将冒号前的值做冒号后处理
    sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
    head = 0
    tail = len(nums) - 1
    sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    while sum_result != target:
        if sum_result > target:
            tail -= 1
        elif sum_result < target:
            head += 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    return [sorted_id[head], sorted_id[tail]]


# 最优方法，python字典采用hash表结构，hash表的查找复杂度近似于O(1) ！！重点！！
def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
    return None