from typing import List

import operator

def addOperators(num: str, target: int) -> List[str]:
    
    def backtrack(idx, total, prev_operand, path):
        
        if idx == len(num):
            if total == target:
                result.append("".join(path))
            return
        
        for i in range(idx, len(num)):
            val = num[idx:i + 1]
            int_val = int(val)

            if idx == 0:
                path.append(val)
                backtrack(i + 1, int_val, int_val, path)
                path.pop()
            else:
                # Addition
                path.append("+" + val)
                backtrack(i + 1, total + int_val, int_val, path)
                path.pop()
                
                # Subtraction
                path.append("-" + val)
                backtrack(i + 1, total - int_val, -int_val, path)
                path.pop()
                
                # Multiplication
                path.append("*" + val)
                # We subtract the last operand and add (last_operand * current_val)
                backtrack(i + 1,  total - prev_operand + (prev_operand * int_val), prev_operand * int_val, path)
                path.pop()
    result = []
    backtrack(0, 0, 0, [])
    return result