"""
给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
返回这两个区间列表的交集。（形式上，闭区间[a, b]（其中a <= b）表示实数x的集合，而a <= x <= b。
两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

示例：
输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""


def intervalIntersection(A: list, B: list) -> list:
    a_n, b_n = len(A), len(B)
    a_idx, b_idx = 0, 0
    ans = []
    # 拉链法（双指针分别指向A，B的头元素，谁的右边界小谁后退一位）
    while a_idx < a_n and b_idx < b_n:
        start = max(A[a_idx][0], B[b_idx][0])
        if A[a_idx][1] < B[b_idx][1]:
            end = A[a_idx][1]
            a_idx += 1
        elif A[a_idx][1] > B[b_idx][1]:
            end = B[b_idx][1]
            b_idx += 1
        else:
            end = A[a_idx][1]
            a_idx += 1
            b_idx += 1
        if start <= end:
            ans.append([start, end])
    return ans


print(intervalIntersection([[1,2]], []))