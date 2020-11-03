"""
给定一个正整数数组nums。

找出该数组内乘积小于k的连续的子数组的个数。

示例 1:
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5],
 [5,2], [2,6], [5,2,6]。需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
"""


def numSubarrayProductLessThanK(nums: list, k: int) -> int:
    start, product, ans = 0, 1, 0
    for end in range(len(nums)):
        product *= nums[end]
        if product >= k:
            product /= nums[start]
            start += 1
        # 每新增一个数字，子数组增加由它开始的逆向累乘数组。
        ans += end - start + 1
    return ans


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
