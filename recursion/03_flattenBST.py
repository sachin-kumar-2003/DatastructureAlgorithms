#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def flattenBST(self, root):
        
        def recursion(root):
            if not root:
                return root
            
            head=recursion(root.left)
            root.left=None
            root.right=recursion(root.right)
            
            if head:
                temp=head
                while temp and temp.right:
                    temp=temp.right
                temp.right=root
                
            else:
                head=root
            return head
        return recursion(root)