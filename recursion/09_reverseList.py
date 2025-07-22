# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def recursion(head):
        if head == None or head.next == None:
            return head
        newHead = recursion(head.next)
        head.next.next = head
        head.next = None
        return newHead

    return recursion(head)      

           
           