from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 计算两个数的最大公约数
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next.val
            b = prev.next.next.val
            greatest_common_divisor = self.gcd(a, b)

            new_node = ListNode(greatest_common_divisor)
            new_node.next = prev.next.next
            prev.next.next = new_node

            prev = prev.next.next

        return dummy.next

# 创建链表 [18, 6, 10, 3]
head = ListNode(18)
head.next = ListNode(6)
head.next.next = ListNode(10)
head.next.next.next = ListNode(3)

# 实例化 Solution 类
solution = Solution()

# 调用方法并得到处理后的链表头节点
new_head = solution.insertGreatestCommonDivisors(head)

# 遍历链表并输出结果
result = []
while new_head:
    result.append(new_head.val)
    new_head = new_head.next

print(result)
