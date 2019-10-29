"""
功能：实现中文数字到阿拉伯数字的转换
解题思路：构建一个中文数字类型和阿拉伯数字对应的字典
再创建一个包含'拾，佰，仟，万，亿'的列表
再创建一个空列表，用来存放对应的数字
依次遍历中文类型数字，判断该数字是否在列表中，是的话进行下一次遍历，否则根据字典输出对应值
作者：郭辉铭。2019.10.29
"""
def chinesetoarab(chinese_number):
    list = ['拾', '佰', '仟', '万', '亿']
    dict = {
        '零': 0,
        '壹': 1,
        '贰': 2,
        '叁': 3,
        '肆': 4,
        '伍': 5,
        '陆': 6,
        '柒': 7,
        '捌': 8,
        '玖': 9,
    }
    arab_number = []
    j = 0
    for i in range(len(chinese_number)):
        if chinese_number[i] in list:
            continue
        else:
            arab_number.append(dict[chinese_number[i]])
            j += 1
    number = [str(k) for k in arab_number]
    return ''.join(number)
str1 = '叁拾柒万陆仟捌佰零壹'
print(chinesetoarab(str1))
