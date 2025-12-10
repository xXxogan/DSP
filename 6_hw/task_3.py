from task_1 import Heap


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False


def kruskal(n, edges):
    edge_heap = Heap()

    for u, v, weight in edges:
        edge_heap.add((weight, u, v))

    uf = UnionFind(n)
    mst = []
    total_weight = 0

    while edge_heap.heap and len(mst) < n - 1:
        weight, u, v = edge_heap.remove_min()
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


if __name__ == "__main__":
    print("Алгоритм Крускала")

    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

    mst, weight = kruskal(4, edges)
    print("Минимальное остовное дерево:", mst)
    print("Общий вес:", weight)
