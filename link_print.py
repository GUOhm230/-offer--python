# -*- coding:utf-8 -*-
"""
问题：python中如何创建单链表:创建节点对象，对每个传入的数据进行一一对应
栈是怎么实现的：建立列表，逐个将列表中的元素中的元素放进列表
列表中的元素再用pop()依次出栈
"""


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def link_print(self, list_node):
        # write code here

        # write code here
        stack = []
        result_array = []
        node_p = list_node.next
        # 将单链表中的值逐个读入栈中
        while node_p:
            stack.append(node_p.data)
            node_p = node_p.next
        # 构建一个新的列表，逐个元素加入该列表
        while stack:
            result_array.append(stack.pop())  # 出栈相应元素，并且删除
        return result_array


if __name__ == "__main__":
    i = 1
    # 链表头结点,头结点是标注链表的唯一指标
    head = ListNode(None)
    cur = head
    while i < 8:
        tmp = ListNode(i)
        tmp.data = i
        tmp.next = None
        cur.next = tmp  # 连接
        cur = tmp
        i += 1
    cur = head.next
    print(Solution().link_print(head))
    list = [1, 2, 3, 4]
    for i in range(4):
        print(list.pop(-1))

