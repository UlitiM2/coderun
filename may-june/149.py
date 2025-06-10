class Heap:
    def __init__(self):
        self.heap = []

    def check_size(self):
        if len(self.heap) == 0:
            return False
        else:
            return True

    def sift_up(self, idx):
        while idx > 0:
            if self.heap[idx] < self.heap[(idx-1)//2]:
                self.heap[idx], self.heap[(idx-1)//2] = self.heap[(idx-1)//2], self.heap[idx]
                idx = (idx-1)//2
            else:
                break

    def sift_down(self, idx):
        len_of_heap = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < len_of_heap and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len_of_heap and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break

            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest

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
mass = list(map(int, input().split()))
sorted_mass = []
new_heap = Heap()

for i in range(n):
    new_heap.input_new(mass[i])

while new_heap.check_size():
    sorted_mass.append(new_heap.extract())

print(*sorted_mass)
