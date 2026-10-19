from typing import List, Optional

def house_robber(nums: List[int]) -> int:

    # we can use a memo or use python @cache. for interviews, use memo. if you run it and its TLE, 
    # convert to using @cache

    def dfs(idx, memo={}):

        if idx in memo:
            return memo[idx]
        
        if idx >= len(nums):
            return 0
        
        skip = 0 + dfs(idx + 1, memo)
        visit = nums[idx] + dfs(idx + 2, memo)

        return max(skip, visit)

    return dfs(0)


# For this problem, nums is circular and if you rob first house, you cannot rob last house. 
# the optimal solution here is to split the problem (nums). if we try robbing house 0 to n - 2 and house 1 - n -1
# last and first house will never be robbed together. The intuitive thing to do is to do a modulo wrap around and remember the last robbed house.
# But that defeats DP as now we are trying to remember things. dp(0) should always be deterministic. With the described solution, dp(0) before remembering is different
# from after. 

# So we call house robber 1 
def house_robber2(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    nums1 = nums[1:]
    nums2 = nums[:-1]

    return max(house_robber(nums1), house_robber(nums2))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

# This is now different in the sense that what's given as input is a binary tree where the thief can 
# only enter from the root and cannot rob directly linked houses. I believe this is the same as house robber 1 but
# with a tree. 
def house_robber3(root: Optional[TreeNode]) -> int:
    
    def dfs(node, memo=None):
        if node in memo:
            return memo[node]
        
        if node is None:
            return 0
        
        skip_total = 0 + dfs(node.left, memo) + dfs(node.right, memo)
        visit_total = node.val

        for child in [node.left, node.right]:
            if child:
                visit_total += dfs(child.left, memo) + dfs(child.right, memo)

        memo[node] = max(visit_total, skip_total)
        return memo[node]
        
    return dfs(root)