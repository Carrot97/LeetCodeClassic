"""
给定一个包含n+1个整数的数组nums，其数字都在1到n之间（包括1和n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2
"""


# 普通圈排序做法，但改变了原数组
def findDuplicate(nums: list) -> int:
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] < 0:
            return idx + 1
        nums[idx] *= -1
    return -1


# 快慢指针+圈排序思想(由于存在重复元素，因此圈排序思想中圈中必然有一个小圈)
def findDuplicate2(nums: list) -> int:
    fast = slow = 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        if fast == slow:
            fast = 0
            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            return slow


print(findDuplicate([1, 3, 4, 2, 2]))
