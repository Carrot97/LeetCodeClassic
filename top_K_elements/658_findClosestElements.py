"""
给定一个排序好的数组，两个整数k和 x，从数组中找到最靠近x（两数之差最小）的k个数。
返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

示例1:
输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]
"""
import heapq


# 堆方法 O(NlogN)
def findClosestElements(arr: list, k: int, x: int) -> list:
    heap = []
    for n in arr[:k]:
        heapq.heappush(heap, (-abs(x - n), n))
    for n in arr[k:]:
        val = -abs(x - n)
        if val > heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (-abs(x - n), n))
    return sorted([n[1] for n in heap])


# 双指针 + 二分查找  O(logN+K)
def findClosestElements2(arr: list, k: int, x: int) -> list:
    n = len(arr)
    left = 0
    right = n - k
    while left < right:
        mid = left + (right - left) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]


print(findClosestElements2([1, 2, 3, 4, 5], 4, 3))
