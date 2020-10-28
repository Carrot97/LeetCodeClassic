"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


def merge(intervals: list) -> list:
    intervals.sort(key=lambda k: k[0])
    ans = []
    if intervals:
        ans.append(intervals[0])
    for interval in intervals[1:]:
        if interval[0] > ans[-1][1]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
    return ans


print(merge([[1,4],[0,4]]))
