def threeSumClosest(nums: list, target: int) -> int:
    def helper(ans, diff, a, b, c):
        val = a + b + c
        diff_ = abs(val - target)
        if diff_ < diff:
            diff = diff_
            ans = val
        return ans, diff

    n = len(nums)
    nums.sort()
    diff = 1e8
    ans = 0
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        third = n - 1
        for second in range(first + 1, n):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            while second < third and nums[second] + nums[third] + nums[first] > target:
                third -= 1
            if third + 1 < n:
                ans, diff = helper(ans, diff, nums[first], nums[second], nums[third + 1])
            if second == third:
                break
            ans, diff = helper(ans, diff, nums[first], nums[second], nums[third])
    return ans




print(threeSumClosest([1, 1, -1], 0))
