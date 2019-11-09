"""
代码功能：实现快速排序算法
"""


def partition(list1, low, high):
    """
    实现快速排序中的一趟排序
    """
    pivot = list1[low]
    while low < high:  # 外层循环，按每次交换一次high和low的位置为终结
        while low < high and list1[high] >= pivot:  # 直至找到右边中有比pivot小的元素为止，并将其放入该处，于是之后的high处位置空余出来
            high -= 1
        list1[low] = list1[high]
        while low < high and list1[low] <= pivot:  # 找到一个比轴元素更大的元素为止，将其放入空位中
            low += 1
        list1[high] = list1[low]
    list1[low] = pivot
    return low  # 返回的是基准值最后安放的位置


def quick_sort(list1, low, high):
    if low < high:
        pivotpos = partition(list1, low, high)
        quick_sort(list1, low, pivotpos-1)
        quick_sort(list1, pivotpos+1, high)
    return list1


list1 = [1, 2, 5, 4, 3, 9, 7, 11, 6, 10, 8]
high = len(list1)-1
print(quick_sort(list1, 0, high))
