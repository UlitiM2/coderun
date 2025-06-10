class Heap:
    def __init__(self):
        self.heap = []

    def sift_up(self, idx):
        while idx > 0:
            if self.heap[idx] > self.heap[(idx-1)//2]:
                self.heap[idx], self.heap[(idx-1)//2] = self.heap[(idx-1)//2], self.heap[idx]
                idx = (idx-1)//2
            else:
                break

    def sift_down(self, idx):
        len_of_heap = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if left < len_of_heap and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len_of_heap and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == idx:
                break

            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest

    def input_new(self, num):
        self.heap.append(num)
        self.sift_up(len(self.heap) - 1)

    def extract(self):
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return max_val


n = int(input())
new_heap = Heap()

for _ in range(n):
    request = input().split()
    if request[0] == '0':
        new_heap.input_new(int(request[1]))
    if request[0] == '1':
        print(new_heap.extract())



