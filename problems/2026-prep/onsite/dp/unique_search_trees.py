
# LC 96: 
def numTrees(n: int) -> int:
    memo = {}

    def dfs(nodes):
        if nodes <= 1:
            return 1

        if nodes in memo:
            return memo[nodes]

        total_bsts = 0
        for root in range(1, nodes + 1):
            left_nodes = root - 1
            right_nodes = nodes - root

            total_bsts += dfs(left_nodes) * dfs(right_nodes)

        memo[nodes] = total_bsts
        return total_bsts

    return dfs(n)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# LC 95
def  generateTrees(n: int):

    if n == 0:
        return []

    def build_trees(start, end):
        if start > end:
            return [None]

        all_valid_trees = []

        for i in range(start, end + 1):
            left_branches = build_trees(start, i - 1)
            right_branches = build_trees(i + 1, end)

            for l_branch in left_branches:
                for r_branch in right_branches:
                    current_root = TreeNode(i)
                    current_root.left = l_branch
                    current_root.right = r_branch

                    all_valid_trees.append(current_root)

        return all_valid_trees
    
    return build_trees(1, n)