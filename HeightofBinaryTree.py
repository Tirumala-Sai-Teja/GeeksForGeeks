'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if not root:
            return 0
        if root.left and root.right:
            return 1+max(self.height(root.left),self.height(root.right))
        elif root.left and not root.right:
            return 1+self.height(root.left)
        elif not root.left and root.right:
            return 1+self.height(root.right)
        return 1
        
