class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def is_valid(node: TreeNode, i: int) -> bool:
            if not node or node.val != arr[i]: return False
            if i == len(arr) - 1: return not node.left and not node.right
            return is_valid(node.left, i + 1) or is_valid(node.right, i + 1)
        return is_valid(root, 0)