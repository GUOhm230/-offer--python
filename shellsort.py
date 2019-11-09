def shellsort(insert_list):
    # 第一层循环表示第几趟排序
    j = int(len(insert_list)/2)
    while j >= 1:
        for i in range(1, len(insert_list)):
            if insert_list[i] >= insert_list[i - 1]:
                continue
            else:
                temp = insert_list[i]
                j = i - 1
                # 本层循环，对当前这趟排序进行移动处理。注意是j+1位置才是最终元素插入位置，而j是当前比较的那个元素、总之是插入在其后
                while j >= 0 and temp <= insert_list[j]:
                    insert_list[j + 1] = insert_list[j]
                    j -= 1
            insert_list[j + 1] = temp
        j = int(j/2)
    return insert_list


list = [1, 2, 5, 4, 3, 9]
print(shellsort(list))