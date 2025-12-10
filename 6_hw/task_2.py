from task_1 import Heap


def heap_sort(arr):
    heap = Heap()

    for val in arr:
        heap.add(val)

    sorted_arr = []
    while heap.heap:
        sorted_arr.append(heap.remove_min())

    return sorted_arr


print("Пирамидальная сортировка")
arr = [5, 2, 8, 1, 9, 3]
print("Исходный массив:", arr)
print("Отсортированный массив:", heap_sort(arr))
