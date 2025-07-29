'''25. Reverse Nodes in k-Group'''
from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseList(head1, head2):
            prev = head2
            while head1 != head2:
                nextNode = head1.next
                head1.next = prev
                prev = head1
                head1 = nextNode
            return prev

        def recursion(head):
            first = head
            temp = head

            for _ in range(k):
                if not temp:
                    return first
                temp = temp.next
            second = temp

            newHead = reverseList(first , second)
            first.next = recursion(second)
            return newHead

        return recursion(head)