# -*- coding: utf-8 -*-
#！usr/bin/env python
# str = "aabbbcdsse"
# str2 = set(str)
# print(str2)
# str2.add("a")
# print(len(str2))
# s = set()
# s.add("a")
# print(s)
# if "b" in s:
#     print("hello")
# else:
#     print("guo")
"""
代码功能：求最长不连续子串
思想描述：
"""


def  max_length_substring(s):
    s1 = []  # 开辟一个集合，储存当前字符
    count = 0  # 记录当前连续出现不重复字符的个数
    s_length = []  # 将个数记录
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    else:
        for i in range(len(s)):
            if s[i] in s1:  # 如果该元素已经在集合中则停止添加并重置
                s_length.append(count)  # 个数计入数组后置为0
                count = len(s1)-s1.index(s[i])
                s1.append(s[i])  # 将当前字符加入该集合中
                s1 = s1[s1.index(s[i]):]  # 直接将集合重置
            else:
                count += 1  # 若当前没有重复字符，则计数加一
                s1.append(s[i])  # 将不重复的元素加入其中
        if len(s_length) <= 1:
            return count+1
        else:
            max = s_length[0]
            for j in range(1, len(s_length)):
                if s_length[j] > max:
                    max = s_length[j]
        return s_length



s = "aabsdfcsjkjdnksnksnjs"
s1 = "abcd"
print(len(s1))
print(s1.index("b"))
print(max_length_substring(s))