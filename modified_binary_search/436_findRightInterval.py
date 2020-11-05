"""
给定一组区间，对于每一个区间 i，检查是否存在一个区间 j，它的起始点大于或等于区间 i
的终点，这可以称为 j 在 i 的“右侧”。

示例 1:
输入: [ [1,2] ]
输出: [-1]
解释:集合中只有一个区间，所以输出-1。

示例 2:
输入: [ [3,4], [2,3], [1,2] ]
输出: [-1, 0, 1]
解释:对于[3,4]，没有满足条件的“右侧”区间。
对于[2,3]，区间[3,4]具有最小的“右”起点;
对于[1,2]，区间[2,3]具有最小的“右”起点。
"""


def findRightInterval(intervals: list) -> list:
    voc, ans_dict = {}, {}
    for idx, interval in enumerate(intervals):
        voc[interval[0]] = idx
    intervals.sort(key=lambda k: k[0])
    n = len(intervals)
    # 尾部增加哨兵
    intervals.append([1e8, 1e8+1])
    voc[1e8] = -1
    for idx, interval in enumerate(intervals[:-1]):
        lo, hi = idx + 1, n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if intervals[mid][0] < interval[1]:
                lo = mid + 1
            else:
                hi = mid - 1
        ans_dict[interval[0]] = intervals[lo][0]
    ans = [0] * n
    for k, v in voc.items():
        if k != 1e8:
            ans[v] = voc[ans_dict[k]]
    return ans


print(findRightInterval([]))

