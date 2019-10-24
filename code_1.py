"""
功能：本段代码实现数组中重复数字的提取
思想：依次遍历后续元素进行比较。时间复杂度为O(n^2)
"""

def Repeat_query1(list_1):
    l = len(list_1)
    ran_l = range(l)
    if l == 0 or l == 1:
        print("数组太短不存在重复数组")
    else:
        print("数组中的重复元素有：")
        for i in ran_l:
            for j in ran_l[i+1:]:
                if list_1[j] == list_1[i]:
                    print(list_1[i])
                    break
                else:
                    continue


if __name__ =="__main__":
    list_1 = [2, 3, 1, 0, 2, 5, 3]
    Repeat_query1(list_1)