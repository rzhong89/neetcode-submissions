# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondList = slow.next

        # slice it
        slow.next = None

        # reverse 2nd list
        prev = None
        curr = secondList

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        secondList = prev

        # reorder
        firstList = head

        while secondList:
            temp1, temp2 = firstList.next, secondList.next

            firstList.next = secondList
            secondList.next = temp1
            
            firstList, secondList = temp1, temp2
