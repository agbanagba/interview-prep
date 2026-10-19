class Solution:
    def canCross(self, stones: list[int]) -> bool:
        # 1. Convert the list of stones into a Hash Set. 
        # This gives us O(1) instant lookups when we ask "Is there a stone at position X?"
        stone_set = set(stones)
        
        # We need to know where the finish line is
        last_stone = stones[-1]
        
        # Memoization dictionary to store states we've already calculated
        # Key: (current_position, previous_jump_size) -> Value: Boolean
        memo = {}

        def dfs(current_pos, jump_size):
            # Base case: We reached the final stone!
            if current_pos == last_stone:
                return True
                
            state = (current_pos, jump_size)
            if state in memo:
                return memo[state]

            # 2. YOUR NATURAL INSTINCT: Calculate the 3 exact landing spots
            # We must jump either k-1, k, or k+1
            for next_jump in (jump_size - 1, jump_size, jump_size + 1):
                
                # The frog must actually move forward (no jumping 0 or negative distances)
                if next_jump > 0:
                    landing_spot = current_pos + next_jump
                    
                    # 3. Check if a stone exists exactly where we landed
                    if landing_spot in stone_set:
                        
                        # If a stone is there, jump to it! Pass our current jump_size forward.
                        if dfs(landing_spot, next_jump):
                            memo[state] = True
                            return True
            
            # If we try all 3 jumps and none of them lead to the finish line
            memo[state] = False
            return False

        # Edge Case: The first jump MUST be exactly 1 unit (from stone 0 to stone 1)
        # If there is no stone at position 1, the frog immediately drowns.
        if 1 not in stone_set:
            return False
            
        # Start the search from position 1, with a jump_size of 1
        return dfs(1, 1)