# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr1, curr2 = list1, list2
        i = 0
        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                temp = curr1.next
                curr1.next = curr2
                curr1 = temp
            else:
                temp = curr2.next
                curr2.next = curr1
                curr2 = temp

