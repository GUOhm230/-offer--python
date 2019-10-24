"""
功能:替换字符串中的空格并以%20来表示
实现：先检测出字符串中共有多少空格，然后从后面开始移动，逐个进行扫描遍历
如果未遇到空格则在之前记录的存放字符的最后一个字符位置之前进行填充该字符
如果遇到的是空格，则在之前进行%20字符。直到读完最后一个空格结束！
"""
# 问题：字符串形式中的数组可以加长内存嘛:长度可以增加，但是不能直接搞定


def spaces_replaced(str1):
    str_l = len(str1)
    blank_count = 0
    for i in str1:
        if i == " ":
            blank_count += 1
        else:
            continue
    str_l1 = str_l + 2*blank_count
    new_str = [" "] * str_l1
    k = str_l1-1
    j = str_l-1
    # 一个字符占一个字节，一个空格替换成%20三个字符
    for j in range(str_l):
        if str1[str_l-j-1] == ' ':
            new_str[k] = "0"
            new_str[k-1] = "2"
            new_str[k-2] = "%"
            k -= 3
        else:
            new_str[k] = str1[str_l-j-1]
            k -= 1
    return "".join(new_str)  # 输出字符串，，每个字节中间用什么分隔开


if __name__ == "__main__":
    print(spaces_replaced('We Are Happy'))



