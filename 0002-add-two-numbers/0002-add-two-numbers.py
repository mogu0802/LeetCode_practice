# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)                 ###建立一個0的起點
        current = dummy                     ###接續節點
        carry = 0                           ###進位
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0      ###沒了就當作0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10             ###取商計算這個節點有沒有需要進位
            num  = total % 10               ###取餘得出這格的值
            current.next = ListNode(num)    ###得到新答案
            current = current.next          ###儲存到下一個
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next                   ###不用起點從0後面開始
