"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
你的KthLargest类需要一个同时接收整数k和整数数组nums的构造器，它包含数据流中的初始元素。
每次调用KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);// returns 4
kthLargest.add(5);// returns 5
kthLargest.add(10);// returns 5
kthLargest.add(9);// returns 8
kthLargest.add(4);// returns 8
"""
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list):
        self.heap = []
        self.count = 0
        self.cap = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if self.count < self.cap:
            heapq.heappush(self.heap, val)
            self.count += 1
        else:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]


kthLargest = KthLargest(3, [])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
