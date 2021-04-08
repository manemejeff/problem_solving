"""
100. Same Tree
Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false



Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __eq__(self, other):
    #     if isinstance(self, TreeNode) and isinstance(other, TreeNode):
    #         if isinstance(self.left, TreeNode) and isinstance(self.right, TreeNode) \
    #                 and isinstance(other.left, TreeNode) and isinstance(other.right, TreeNode):
    #             if self.val == other.val and self.left.val == other.left.val \
    #                     and self.right.val == other.right.val:
    #                 return True
    #     else:
    #         return False


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if isinstance(p, TreeNode) and isinstance(q, TreeNode):
            if isinstance(p.left, TreeNode) and isinstance(p.right, TreeNode) \
                    and isinstance(q.left, TreeNode) and isinstance(q.right, TreeNode):
                if p.val == q.val and p.left.val == q.left.val \
                        and p.right.val == q.right.val:
                    return True
        else:
            return False