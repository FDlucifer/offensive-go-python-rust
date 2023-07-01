from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # 哑节点
        current = dummy  # 当前节点
        carry = 0  # 进位

        while l1 or l2:
            # 获取l1和l2的值，如果链表已经遍历完，则值为0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # 将l1和l2的值以及进位相加
            sum = x + y + carry

            # 更新进位
            carry = sum // 10

            # 创建新节点，并将个位数作为节点的值
            current.next = ListNode(sum % 10)

            # 更新指针
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 如果最后一位相加后产生了进位，需要添加新节点
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


s = Solution()
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
print(s.addTwoNumbers(l1, l2))
