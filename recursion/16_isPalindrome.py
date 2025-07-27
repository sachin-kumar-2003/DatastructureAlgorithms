# Definition for singly-linked list.
'''234. Palindrome Linked List'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
            
        def findMid(head1, head2, prev):
            if head2 is None or head2.next is None:
                if head2 is None:  
                    newHead = head1
                    if prev:
                        prev.next = None  
                else:  
                    newHead = head1.next
                    head1.next = None  
                return newHead
            return findMid(head1.next, head2.next.next, head1)
                
        def reverseList(head2):
            if head2 is None:
                return head2
            if head2.next is None:
                return head2
            newHead = reverseList(head2.next)
            head2.next.next = head2
            head2.next = None
            return newHead
                
        def checkPalindrome(head1, head2):
            if head1 is None or head2 is None:
                return True
            if head1.val != head2.val:
                return False
            return checkPalindrome(head1.next, head2.next)
        
        head1 = head
        head2 = findMid(head, head, None)  
        head2 = reverseList(head2)
        return checkPalindrome(head1, head2)