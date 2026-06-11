
from typing import List

def partition(s: str) -> List[List[str]]:

    result = []

    def is_palindrome(ss: str) -> bool:
        return ss == ss[::-1]

    def backtrack(idx, path):
        
        if idx == len(s):
            result.append(path[:])
            return

        # Now the expanding chunks part of the problem
        for end_idx in range(idx + 1, len(s) + 1):
            # Take +1 increasing slice of s
            current_slice = s[idx:end_idx]

            if not is_palindrome(current_slice):
                continue
            
            path.append(current_slice)
            backtrack(end_idx, path)
            path.pop()


    backtrack(0, [])
    return result