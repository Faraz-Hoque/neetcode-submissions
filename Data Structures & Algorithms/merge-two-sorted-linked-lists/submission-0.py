# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            # check which node and from which list to insert into tail list
            if list1.val < list2.val:
                tail.next = list1    # next node in tail = the current node in list1
                list1 = list1.next   # move current node in list1 one step forward
            else:
                tail.next = list2    
                list2 = list2.next

            tail = tail.next      # moving tail one step forward

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next         # head of new sorted list




