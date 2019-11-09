"""
代码功能：实现冒泡排序,小数往上冒
"""
def bubble_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        for i in range(len(list1)):
            flag = False  # 考虑代码健壮性，有时并不需要完全排序 ，如果该趟没有发生数据交换，则说明表本来有序
            j = len(list1)-1
            while j > i:
                if list1[j] < list1[j-1]:
                    temp = list1[j]
                    list1[j] = list1[j-1]
                    list1[j-1] = temp
                    flag = True
                j -= 1
            if flag == False:
                return list1
        return list1


if __name__ == '__main__':
    for i in range(1, 5):
        if i % 2 == 0:
            print(i)
        else:
            continue
        print("continue test")
    list2 = [1, 2, 33, 6, 3, 89, 4, 5]
    list1 = [1]
    print(bubble_sort(list2))
