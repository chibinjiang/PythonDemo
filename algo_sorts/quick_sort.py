"""
快速排序
"""
import time
from random import shuffle
from typing import List


def partition(arr, left: int, right: int):
    i = left
    j = right
    while i < j:
        print(i, j)
        while i < j and arr[j] >= arr[left]:
            j -= 1
        while i < j and arr[i] <= arr[left]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[left] = arr[left], arr[i]
    return i


def quick_sort(arr: List[int], left: int, right: int):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


if __name__ == '__main__':
    start_time = time.time()
    example = list(range(1, 10))
    shuffle(example)
    print("Before:  ", example)
    quick_sort(example, 0, len(example) - 1)
    print("After: ", example)
    print(f"耗时: {time.time() - start_time:.2f} Seconds")
