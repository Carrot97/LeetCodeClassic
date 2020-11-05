class Heap:
    def __init__(self, arr: list):
        self.data = arr
        self.n = len(arr)
        self.heapify()

    # 大根堆
    def heapify(self):
        for idx in range(self.n // 2 - 1, -1, -1):
            self.sink(idx)

    def add(self, num):
        self.data.append(num)
        self.n += 1
        self.float(self.n - 1)

    def sink(self, i):
        while 2 * i + 1 <= self.n - 1:
            j = 2 * i + 1
            if j < self.n - 1 and self.data[j] < self.data[j + 1]:
                j += 1
            if self.data[i] > self.data[j]:
                break
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i = j

    def float(self, i):
        while i > 0:
            j = (i + 1) // 2 - 1
            if self.data[i] <= self.data[j]:
                break
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i = j

    # 堆排序(下沉法)
    def sort(self, arr: list):
        n = self.n
        while n > 1:
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            n -= 1
            self.sink(0)


nums = [3,2,1,5,6,4]
heap = Heap(nums)
print(heap.data)
heap.add(5)
print(heap.data)

