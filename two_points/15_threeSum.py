def threeSum(nums: list) -> list:
    n = len(nums)
    nums.sort()
    ans = []
    for first in range(n - 2):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        # 提升性能
        # if nums[first] + nums[first + 1] + nums[first + 2] > 0:
        #     break
        # if nums[first] + nums[n - 2] + nums[n - 1] < 0:
        #     continue
        third = n - 1
        target = -nums[first]
        for second in range(first + 1, n - 1):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])
    return ans


print(threeSum([-2, 0, 1, 1, 2]))
