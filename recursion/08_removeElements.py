# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List,Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        def recursion(head,val):
            if head == None:
                return None
            head.next = recursion(head.next,val)
            if head.val == val:
                return head.next
            else:
                return head
        
        return recursion(head,val)