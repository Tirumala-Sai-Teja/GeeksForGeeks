class Solution:
    def hasPathSum(self,root, S):
        if not root:
            return False
        target=S-root.data
        if not root.left and not root.right:
            if target==0:
                return True
            else:
                return False
        return self.hasPathSum(root.left,target) or self.hasPathSum(root.right,target)
