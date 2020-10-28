"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，
要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
"""


def sortedSquares(A: list) -> list:
    n = len(A)
    left = -1
    for i in range(n-1):
        if A[i] < 0:
            left = i
        else:
            break
    ans, right = [], left + 1
    while left >= 0 or right < n:
        if left < 0:
            ans.append(A[right] ** 2)
            right += 1
        elif right >= n:
            ans.append(A[left] ** 2)
            left -= 1
        elif abs(A[left]) <= abs(A[right]):
            ans.append(A[left] ** 2)
            left -= 1
        else:
            ans.append(A[right] ** 2)
            right += 1
    return ans


print(sortedSquares([-2, 0]))
