class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.best = 1
        def depth(root):
            if not root: return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR + 1)
            return 1 + max(ansL, ansR)
        
        depth(root)
        return self.best - 1