"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
[2,3,4]的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.len = 0
        # lo作为大根堆存储较小的一半
        self.lo = []
        # lo作为大根堆存储较小的一半
        self.hi = []
        # 两堆顶元素即为中位数

    def addNum(self, num: int) -> None:
        self.len += 1
        # 由于python只有小根堆，因此大根堆采用负数存储
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # 只允许lo比hi多存一个数， （& 1 ==）即为（% 2 ！=）
        if self.len & 1 != 0:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if self.len & 1 != 0:
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
