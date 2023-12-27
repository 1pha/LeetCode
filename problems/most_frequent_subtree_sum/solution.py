from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]: 
        self.counter = dict()
        def add_to_dict(key):
            if key in self.counter:
                self.counter[key] += 1
            else:
                self.counter[key] = 1

        def get_subtree_sum(root: TreeNode):
            if (root.left is None) and (root.right is None):
                add_to_dict(key=root.val)
                return root.val
            else:
                val = root.val
                if root.left is not None:
                    subval = get_subtree_sum(root.left)
                    val += subval
                if root.right is not None:
                    subval = get_subtree_sum(root.right)
                    val += subval
                add_to_dict(key=val)
                return val
        
        get_subtree_sum(root=root)
        most_list, most_count = [], 0
        for subsum in self.counter:
            _count = self.counter[subsum]
            if _count > most_count:
                most_list = [subsum]
                most_count = _count
            elif _count == most_count:
                most_list.append(subsum)
            else:
                continue
        return most_list


if __name__=="__main__":
    sol = Solution()
    print(sol.findFrequentTreeSum(root=TreeNode(val=5,
                                                left=TreeNode(val=2, left=None, right=None),
                                                right=TreeNode(val=-3, left=None, right=None))))
    print(sol.findFrequentTreeSum(root=TreeNode(val=5,
                                                left=TreeNode(val=2, left=TreeNode(val=2), right=TreeNode(val=3)),
                                                right=TreeNode(val=-3, left=TreeNode(val=4), right=TreeNode(val=1)))))
    print(sol.findFrequentTreeSum(root=TreeNode(val=3,
                                                left=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=2, left=TreeNode(val=3))),
                                                right=TreeNode(val=5, left=TreeNode(val=4), right=TreeNode(val=6)))))