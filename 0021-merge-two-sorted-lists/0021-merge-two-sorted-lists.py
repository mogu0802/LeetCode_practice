# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(0)
        num = first
        while list1 and list2:                  ###如果其中一個還有東西
            if list1.val < list2.val:           ###誰小存誰的頭
                num.next = list1
                list1 = list1.next
            else:
                num.next = list2
                list2 = list2.next
            num = num.next                      ###移動到下一個儲存格
        num.next = list1 if list1 else list2    ###看誰的還有剩全部排進去
        return first.next
        