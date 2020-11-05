"""
给定一个n x n矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
"""
import heapq


def kthSmallest(matrix: list, k: int) -> int:
    n = len(matrix)
    heap = []
    for i in range(n):
        heapq.heappush(heap, (matrix[i][0], i, 0))
    for _ in range(k - 1):
        num, x, y = heapq.heappop(heap)
        if y != n - 1:
            heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
    return heap[0][0]


print(kthSmallest([
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
], 8))
