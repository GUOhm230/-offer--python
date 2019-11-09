"""
代码功能：实现折半插入排序
"""
def insert_sort(list1):
    for i in range(1, len(list1)):
        temp = list1[i]  # 记录当前需要进行排列的元素，空出该位置，方便之后的移动
        low = 0
        high = i-1

        while low <= high:
            mid = int((low+high)/2)  # 此处要注意，需要取其中整数，不能直接除
            if list1[mid] < temp:
                low = mid+1
            else:
                high = mid-1
        j = i-1
        while j >= high:
            list1[j+1] = list1[j]
            j -= 1
        list1[high+1] = temp  # 每次循环得到一个局部排序的顺序表
    return list1


list = [1, 2, 5, 4, 3, 9]
print(insert_sort(list))

