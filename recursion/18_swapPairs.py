'''24. Swap Nodes in Pairs'''
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def recursion(head):
        if head is None or head.next is None:
            return head
        first = head
        second = head.next

        first.next = recursion(second.next)
        second.next = first
        return second
    
    return recursion(head)