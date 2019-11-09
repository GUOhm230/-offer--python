"""
功能：实现列表的直接插入排序
思想：第i趟排序，对前i个元素进行排序，将L[i]与前面的元素进行比较，将比其小的元素后移
注意：在很难实现从尾到头实现依次遍历时，应该使用while，不应该纠结于for循环
时间复杂度O(n^2)
"""


def direct_insertion(insert_list):
    # 第一层循环表示第几趟排序
    for i in range(1, len(insert_list)):
        if insert_list[i] >= insert_list[i-1]:
            continue
        else:
            temp = insert_list[i]
            j = i-1
            # 本层循环，对当前这趟排序进行移动处理。注意是j+1位置才是最终元素插入位置，而j是当前比较的那个元素、总之是插入在其后
            while j >= 0 and temp <= insert_list[j]:
                insert_list[j+1] = insert_list[j]
                j -= 1
        insert_list[j+1] = temp
    return insert_list


L = [1, 25, 6, 7, 2, 8, 3]
print(direct_insertion(L))


