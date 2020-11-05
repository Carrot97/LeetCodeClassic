"""
我们把符合下列属性的数组A称作山脉：
A.length >= 3
存在 0 < i< A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足A[0] < A[1] < ... A[i-1] < A[i]
> A[i+1] > ... > A[A.length - 1]的 i的值。
"""


# 双调二分查找
def peakIndexInMountainArray(arr: list) -> int:
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


print(peakIndexInMountainArray([0, 2, 1, 0]))
