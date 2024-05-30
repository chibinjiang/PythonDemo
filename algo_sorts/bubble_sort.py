"""
冒泡排序
先确定 外循环 (有序部分)
    - 思考起点和终点
        - 终点是否包含最后一个元素
再确定 内循环 (未排序部分)
    - 思考起点和终点
        - 终点是否包含最后一个元素
        - 起点是否包含第一个元素

循环内的操作:
-

评估:
- 一致性:
- 时间复杂度
- 空间复杂度

"""
import time
from random import shuffle


def bubble_sort(arr):
    length = len(arr)
    # 外循环的 范围:
    for i in range(length-1, 0, -1):
        print("外循环到: ", i)
        for j in range(i):
            if arr[j] > arr[j+1]:
                print(f"\t交换: {j} 和 {j+1}")
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


def main():
    start_time = time.time()
    example = list(range(1, 10))
    shuffle(example)
    print("Before: ", example)
    bubble_sort(example)
    print("After: ", example)
    print(f"耗时: {time.time() - start_time:.2f} Seconds")


if __name__ == '__main__':
    main()

