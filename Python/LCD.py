class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p, q)

    def lca(self, curr, p, q):
        if curr == None:
            return
        
        # p as parent
        if curr.val == p.val and ((curr.left and curr.left.val == q.val) or (curr.right and curr.right.val == q.val)):
            return p
        
        # q as parent
        if curr.val == q.val and ((curr.left and curr.left.val == p.val) or (curr.right and curr.right.val == p.val)):
            return q

        # p and q as child
        if (curr.left and curr.right) and ((curr.left.val == p.val and curr.right.val == q.val) or (curr.left.val == q.val and curr.right.val == p.val)):
            print("found!")
            return curr.val
        
        left = self.lca(curr.left, p, q)
        right = self.lca(curr.right, p, q)

