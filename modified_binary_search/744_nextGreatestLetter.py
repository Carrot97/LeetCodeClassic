"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。
另给出一个目标字母target，请你寻找在这一有序列表里比目标字母大的最小字母。
在比较时，字母是依序循环出现的。举个例子：
如果目标字母 target = 'z' 并且字符列表为letters = ['a', 'b']，则答案返回'a'

示例：
输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"
输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"
"""


def nextGreatestLetter(letters: list, target: str) -> str:
    lo, hi = 0, len(letters) - 1
    letters.append(letters[0])
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if letters[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1
    return letters[lo]


print(nextGreatestLetter(["c", "f", "j"], "j"))
