"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：
输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


def helper(n: int):
    res = 0
    while n:
        res += (n % 10) ** 2
        n //= 10
    return res


# 数学算法
def isHappy(n: int):
    # 若不是快乐数则会陷入voc数组死循环
    voc = [4, 16, 37, 58, 89, 145, 42, 20]
    while n != 1 and n not in voc:
        n = helper(n)
    return n == 1


# 快慢指针算法
def isHappy2(n: int):
    fast = slow = n
    while fast != 1:
        slow = helper(slow)
        fast = helper(helper(fast))
        if fast == slow != 1:
            return False
    return True


print(isHappy2(37))
