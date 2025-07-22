# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(head1,head2):
            if head1 is None:
                return head2
            if head2 is None:
                return head1
            if head1.val <= head2.val:
                head1.next = recursion(head1.next,head2)
                return head1
            else:
                head2.next = recursion(head1,head2.next)
                return head2
        return recursion(list1,list2)
            