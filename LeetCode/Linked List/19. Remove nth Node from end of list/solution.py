# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        if count == 0:
            return None
        
        if n == count:
            return curr.next
        while curr:
            count -= 1
            if count == n:
                prev = curr
                curr.next = curr.next.next
                break

            curr = curr.next
        return head