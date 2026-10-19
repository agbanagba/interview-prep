def can_jump(nums: list[int]) -> bool:

    furthest = 0
    for i in range(len(nums)):
        if i > furthest:
            return False
        
        furthest = max(furthest, i + nums[i])
        if furthest >= len(nums) - 1:
            return True
    
    return True


def jumpII(nums: list[int]):
    pass