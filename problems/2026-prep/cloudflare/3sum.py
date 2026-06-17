def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort() # O(nlogn)
    results = []

    n = len(nums)

    for i in range(n - 2):
        
        # Basically, this is saying that if the number is the same as last, we should not bother
        # because we'd end up the same triplets.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

    
        # since we are looking for numbers on the right of the already sorted array, if my current value is greater than zero. 
        # it's impossible to find two greater numbers that will add up.
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
            
    

        return results