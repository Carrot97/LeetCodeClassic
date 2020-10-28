"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠
（如果有必要的话，可以合并区间）。
"""


def insert(intervals: list, newInterval: list) -> list:
    n = len(intervals)
    start, end, idx = 0, n-1, 0
    # 寻找插入左索引
    while idx < n:
        if newInterval[0] <= intervals[idx][0] or newInterval[0] <= intervals[idx][1]:
            start = idx
            break
        idx += 1
    # 若所有区间左右端点都小于新区间左端点，则将新区间添加至末尾
    if idx == n:
        intervals.append(newInterval)
        return intervals

    # 寻找插入右索引
    while idx < n:
        # 注意左边界单独讨论
        if newInterval[1] < intervals[idx][0]:
            end = idx - 1
            break
        elif newInterval[1] <= intervals[idx][1]:
            end = idx
            break
        idx += 1
    # 若新区间右端点小于第一个区间的左端点，则将新区间插入至首位
    if end == -1:
        intervals.insert(0, newInterval)
        return intervals
    # 考虑到合并的情况（确定新区间端点值）
    newInterval[0] = min(newInterval[0], intervals[start][0])
    newInterval[1] = max(newInterval[1], intervals[end][1])
    # 删除被合并的区间
    del intervals[start: end + 1]
    intervals.insert(start, newInterval)
    return intervals


print(insert([], [1,2]))
