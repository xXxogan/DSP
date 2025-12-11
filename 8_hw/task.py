class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, value):
        idx = self._hash(value)
        if value not in self.table[idx]:
            self.table[idx].append(value)

    def remove(self, value):
        idx = self._hash(value)
        if value in self.table[idx]:
            self.table[idx].remove(value)

    def contains(self, value):
        idx = self._hash(value)
        return value in self.table[idx]

    def __str__(self):
        elements = []
        for bucket in self.table:
            elements.extend(bucket)
        return f"{{{', '.join(map(str, elements))}}}"


if __name__ == "__main__":
    print("Множество (HashSet)")
    s = HashSet()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(2)
    print(f"Множество: {s}")
    print(f"Содержит 2? {s.contains(2)}")
    s.remove(2)
    print(f"После удаления 2: {s}")
    print(f"Содержит 2? {s.contains(2)}")


""" 

Множество (HashSet)
Множество: {1, 2, 3}
Содержит 2? True
После удаления 2: {1, 3}
Содержит 2? False

"""
