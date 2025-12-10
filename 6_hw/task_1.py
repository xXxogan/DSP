class Heap:
    def __init__(self):
        self.heap = []

    def add(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def get_max(self):
        if not self.heap:
            return None
        return max(self.heap)

    def remove_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def remove_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_idx = self.heap.index(max(self.heap))
        max_val = self.heap[max_idx]

        last = self.heap.pop()
        if max_idx < len(self.heap):
            self.heap[max_idx] = last
            self._sift_down(max_idx)
            self._sift_up(max_idx)

        return max_val

    def print_heap(self):
        print("Пирамида:", self.heap)

    def _sift_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(parent)

    def _sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._sift_down(smallest)


if __name__ == "__main__":
    print("Очередь по приоритетам")
    h = Heap()
    h.add(5)
    h.add(3)
    h.add(7)
    h.add(1)
    h.print_heap()
    print("Минимум:", h.get_min())
    print("Максимум:", h.get_max())
    print("Удаляем минимум:", h.remove_min())
    print("Удаляем максимум:", h.remove_max())
    h.print_heap()

""" 

Очередь по приоритетам
Пирамида: [1, 3, 7, 5]
Минимум: 1
Максимум: 7
Удаляем минимум: 1
Удаляем максимум: 7
Пирамида: [3, 5]

"""
