# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next #advance to next node
            curr.next=prev  #reverse the pointer from pointing
                            # to next to pointing to prev
            prev=curr       #prev node is now curr node
            curr=nxt        #curr node is now nxt node
        return prev
        