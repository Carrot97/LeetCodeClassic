"""
给你一个 m* n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。

示例 1：
输入：mat = [[1,3,11],[2,4,6]], k = 5
输出：7
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。
"""
import heapq


def kthSmallest(mat, k: int) -> int:
    m, n = len(mat), len(mat[0])
    pointers = [0] * m
    heap = []
    curr_sum = 0
    for i in range(m):
        curr_sum += mat[i][0]
    heapq.heappush(heap, [curr_sum, tuple(pointers)])
    seen = set()
    seen.add(tuple(pointers))
    for _ in range(k):
        curr_sum, pointers = heapq.heappop(heap)
        for i, j in enumerate(pointers):
            if j < n - 1:
                new_pointers = list(pointers)
                new_pointers[i] = j + 1
                new_pointers = tuple(new_pointers)
                if new_pointers not in seen:
                    new_sum = curr_sum + mat[i][j + 1] - mat[i][j]
                    heapq.heappush(heap, [new_sum, tuple(new_pointers)])
                    seen.add(tuple(new_pointers))
    return curr_sum


print(kthSmallest([[1,3,11],[2,4,6]], 9))
