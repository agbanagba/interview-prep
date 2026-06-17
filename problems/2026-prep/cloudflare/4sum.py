def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    results = []
    n = len(nums)

    # First Anchor
    for i in range(n - 3):
        # Skip duplicates for the first anchor
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Second Anchor (starts right after i)
        for j in range(i + 1, n - 2):
            # Skip duplicates for the second anchor
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
                
            # Now we are back in familiar territory! Standard 2-Pointer.
            left, right = j + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if current_sum == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
    return results