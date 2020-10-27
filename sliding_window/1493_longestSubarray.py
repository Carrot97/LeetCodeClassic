def longestSubarray(nums: list) -> int:
    start, ans, last_0 = 0, 0, -1
    for end in range(len(nums)):
        if nums[end] == 0:
            start = last_0 + 1
            last_0 = end
        ans = max(ans, end - start)
    return ans


print(longestSubarray([1]))
