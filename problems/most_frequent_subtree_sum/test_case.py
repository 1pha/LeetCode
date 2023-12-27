from most_frequent_subtree_sum.solution import Solution, TreeNode

def test_case():
    sol = Solution()
    
    root = TreeNode(val=5)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=-3)
    output = [2, -3, 4]
    assert set(sol.findFrequentTreeSum(root=root)) == set(output)
    
    root = TreeNode(val=5)
    root.left = TreeNode(val=2)
    root.left.left = TreeNode(val=-2)
    root.left.right = TreeNode(val=1)
    
    root.right = TreeNode(val=-3)
    root.right.left = TreeNode(val=4)
    root.right.right = TreeNode(val=1)
    output = [1]
    assert set(sol.findFrequentTreeSum(root=root)) == set(output)
    
    root = TreeNode(val=3)
    root.left = TreeNode(val=1)
    root.left.left = TreeNode(val=0)
    root.left.right = TreeNode(val=2)
    root.left.right.left = TreeNode(val=3)
    
    root.right = TreeNode(val=5)
    root.right.left = TreeNode(val=4)
    root.right.right = TreeNode(val=6)
    output = [6]
    assert set(sol.findFrequentTreeSum(root=root)) == set(output)
