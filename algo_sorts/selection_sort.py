"""
选择排序
"""
import time
from random import shuffle


def selection_sort(nums: list[int]):
    """选择排序"""
    n = len(nums)
    # 外循环：未排序区间为 [i, n-1]
    for i in range(n - 1):
        # 内循环：找到未排序区间内的最小元素
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j  # 记录最小元素的索引
        # 将该最小元素与未排序区间的首个元素交换
        nums[i], nums[k] = nums[k], nums[i]


def main():
    start_time = time.time()
    example = list(range(1, 1000))
    shuffle(example)
    print("Before: ", example)
    selection_sort(example)
    print("After: ", example)
    print(f"耗时: {time.time() - start_time:.2f} Seconds")


if __name__ == '__main__':
    main()
