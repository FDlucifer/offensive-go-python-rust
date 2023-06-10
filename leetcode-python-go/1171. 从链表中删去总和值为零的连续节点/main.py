from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 将链表转换为数组
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # 处理该数组以移除sum = 0的子数组
        start = 0
        while start < len(arr):
            total_sum = 0
            end = start
            while end < len(arr):
                total_sum += arr[end]
                if total_sum == 0:
                    break
                end += 1

            if total_sum == 0:
                # 从arr中移除子数组
                del arr[start:end+1]
            else:
                start += 1

        # 将更新后的数组转换为链表
        dummy = ListNode(0)
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next



# Test the solution
if __name__ == "__main__":
    # Create the input linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(-3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(1)

    # Create an instance of the solution class
    solution = Solution()

    # Call the removeZeroSumSublists method
    result = solution.removeZeroSumSublists(head)

    # Print the result
    while result:
        print(result.val, end=" ")
        result = result.next
